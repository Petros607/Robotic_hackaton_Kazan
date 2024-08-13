from src.user import schemas, models_manager
from src.user.token.token import TokenManager
from fastapi import HTTPException
from typing import Tuple
import hashlib




async def add_user(user: schemas.RegisterRequest) -> schemas.RegisterSuccessResponse:
    hasher = hashlib.new("sha256")
    is_login_exists = await models_manager.is_login_exists(user.login)
    if is_login_exists:
        raise HTTPException(status_code=400, detail="This login already exists")
    is_email_exists = await models_manager.is_email_exists(user.email)
    if is_email_exists:
        raise HTTPException(status_code=400, detail="This email already uses")

    hasher.update(user.password.encode())
    password_hash = hasher.hexdigest()
    await models_manager.add_user(
        user.login, password_hash, user.email, user.username, user.sex, user.age
    )


async def login(user: schemas.LoginRequest) -> Tuple[str, str]:
    hasher = hashlib.new("sha256")
    """_summary_

    Args:
        user (schemas.LoginRequest): data from user

    Raises:
        HTTPException: uncorrect login or pasword

    Returns:
        str: access-token, refresh-token
    """
    password_hash = hasher.update(user.password.encode())
    user_id = await models_manager.check_password_hash(
        user.login, password_hash
    )
    if user_id is None:
        raise HTTPException(code = 400, detail = "Uncorrect login or password")
    refresh_token = TokenManager.create_refresh_token(user_id)
    refresh_token_id = await models_manager.add_token(user_id, refresh_token)
    access_token = TokenManager.create_access_token(user_id, refresh_token_id)
    return access_token, refresh_token

async def logout(token: str) -> bool:
    payload = TokenManager.decode_token(token)
    if payload:
        refresh_token_id = payload["refresh_token_id"]
        is_logout = await models_manager.delete_token(refresh_token_id)
        return is_logout
    else:
        raise HTTPException(status_code=401, detail="Invalid access token")
    
    
async def refresh_token(token: str) -> str:
    payload = TokenManager.decode_token(token)
    if payload:
        user_id = payload["user_id"]
    else:
        raise HTTPException(status_code=401, detail="Refresh token is not valid")

    refresh_token_id = await models_manager.check_token(user_id, token)
    if refresh_token_id:
        new_token = TokenManager.create_access_token(user_id, refresh_token_id)
        return new_token
    else:
        raise HTTPException(status_code=401, detail="Refresh token is not valid")
