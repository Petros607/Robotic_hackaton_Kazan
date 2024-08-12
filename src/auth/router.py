from fastapi import APIRouter, Request, HTTPException, Depends
from src.auth import schemas
from fastapi.security import OAuth2PasswordBearer
from src.auth.tokens import TokenManager

router = APIRouter(
    prefix="",
    tags=["Регистриция, авторизация"],
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/register", response_model=schemas.RegisterSuccessResponse)
async def register_user(request: Request, user_data: schemas.RegisterRequest):
    try:
        user_id = await user_manager.add_user(
            login=user_data.login, password=user_data.password
        )
        if user_id:
            return user_models.RegisterSuccessResponse(
                status="success", message="User registered successfully"
            )
        else:
            raise HTTPException(status_code=400, detail="User already exists")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/login", response_model=user_models.AuthResponse)
async def login_user(request: Request, user_data: user_models.RegisterRequest):
    user_id = await user_manager.check_user(user_data.login, user_data.password)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid login or password")
    refresh_token = TokenManager.create_refresh_token(user_id)
    refresh_token_id = await user_manager.add_token(user_id, refresh_token)
    access_token = TokenManager.create_access_token(user_id, refresh_token_id)
    return user_models.AuthResponse(
        status="success",
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="bearer",
        expires_in=TokenManager.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    )


@router.post("/logout")
async def logout_user(request: Request, token: str = Depends(oauth2_scheme)):
    payload = TokenManager.decode_token(token)
    if payload:
        refresh_token_id = payload["refresh_token_id"]
        is_logout = await user_manager.delete_token(refresh_token_id)
        if is_logout:
            return user_models.LogoutSuccessResponse(
                status="success", message="User logout succesfully"
            )
        else:
            raise HTTPException(
                status_code=401,
                detail="Invalid refresh token (maybe you are logout already)",
            )
    else:
        raise HTTPException(status_code=401, detail="Invalid access token")