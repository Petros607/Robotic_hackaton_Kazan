import jwt

from datetime import datetime, timedelta, timezone
from typing import Union

from src.user.token import configs


class TokenManager:
    __SECRET_KEY = configs.SECRET_KEY
    _ALGORITHM = configs.ALGORITHM
    _ACCESS_TOKEN_EXPIRE_MINUTES = configs.ACCESS_TOKEN_EXPIRE_MINUTES
    _REFRESH_TOKEN_EXPIRE_DAYS = configs.REFRESH_TOKEN_EXPIRE_DAYS
    

    header = {"alg": _ALGORITHM, "typ": "JWT"}

    @classmethod
    def create_access_token(cls, user_id: int, refresh_token_id: int):
        payload = {"user_id": user_id, "refresh_token_id": refresh_token_id}
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=cls._ACCESS_TOKEN_EXPIRE_MINUTES
        )
        payload["exp"] = expire
        encoded_jwt = jwt.encode(payload, cls.__SECRET_KEY, algorithm=cls._ALGORITHM)
        return encoded_jwt

    @classmethod
    def create_refresh_token(cls, user_id: int):
        payload = {"user_id": user_id}
        expire = datetime.now(timezone.utc) + timedelta(
            days=cls._REFRESH_TOKEN_EXPIRE_DAYS
        )
        payload["exp"] = expire
        encoded_jwt = jwt.encode(payload, cls.__SECRET_KEY, algorithm=cls._ALGORITHM)
        return encoded_jwt

    @classmethod
    def decode_token(cls, token: str) -> Union[None, dict]:
        try:
            decoded_token = jwt.decode(
                token, cls.__SECRET_KEY, algorithms=[cls._ALGORITHM]
            )
            return (
                decoded_token
                if decoded_token["exp"] >= datetime.now(timezone.utc).timestamp()
                else None
            )
        except jwt.ExpiredSignatureError:
            return None
        except jwt.PyJWTError:
            return None