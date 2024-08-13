from pydantic import BaseModel


class RegisterRequest(BaseModel):
    login: str
    password: str
    email: str
    username: str
    sex: bool
    age: int


class RegisterSuccessResponse(BaseModel):
    status: str
    message: str
    emoji: str


class LoginRequest(BaseModel):
    login: str
    password: str


class AuthResponse(BaseModel):
    status: str
    access_token: str
    refresh_token: str
    token_type: str
    expires_in: int
    emoji: str


class ErrorResponse(BaseModel):
    status: str
    message: str


class LogoutSuccessResponse(BaseModel):
    status: str
    message: str
    emoji: str


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class RefreshTokenSuccessResponse(BaseModel):
    access_token: str
    expires_in: int
    emoji: str


class UpdateUserDataRequest(BaseModel):
    habitation: str | None = None
    validation: bool | None = None
    profession: str | None = None
    address: str | None = None
    marriage_status: bool | None = None


class UpdateUserDataResponse(BaseModel):
    status: str
    message: str
    emoji: str


class UserDataResponse(BaseModel):
    username: str
    email: str
    sex: bool
    age: int
    habitation: str | None
    validation: bool | None
    profession: str | None
    address: str | None
    marriage_status: bool | None
