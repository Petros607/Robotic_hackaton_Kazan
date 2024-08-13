from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from src.user import schemas
from src.user import middleware
from src.user.token.token import TokenManager

router = APIRouter(tags=["User"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post(
    "/register",
    description="Отправка данных о пользователя для регистрации с систему",
    response_model=schemas.RegisterSuccessResponse,
)
async def post_register(request: Request, user_data: schemas.RegisterRequest):
    await middleware.add_user(user_data)
    return schemas.RegisterSuccessResponse(
        status="success", message="User registered successfully", emoji="＼(￣▽￣)／"
    )


@router.post(
    "/login",
    description="Отправка данных о пользователя для входа с систему",
    response_model=schemas.AuthResponse,
)
async def post_login(request: Request, user_data: schemas.LoginRequest):
    access_token, refresh_token = await middleware.login(user_data)
    return schemas.AuthResponse(
        status="success",
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="bearer",
        expires_in=TokenManager._ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        emoji="＼(￣▽￣)／",
    )


@router.post(
    "/logout",
    description="Отправка данных о пользователя для выхода из системы",
    response_model=schemas.LogoutSuccessResponse,
)
async def post_logout(request: Request, token: str = Depends(oauth2_scheme)):
    is_logout = await middleware.logout(token)
    if is_logout:
        return schemas.LogoutSuccessResponse(
            status="success", message="User logout succesfully", emoji="＼(￣▽￣)／"
        )
    else:
        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token (maybe you are logout already)",
        )


@router.post("/update_data", description="Отправка новых данных о пользователе")
async def post_update_data():

    return "＼(￣▽￣)／"
