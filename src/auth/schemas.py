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


class AuthResponse(BaseModel):
    status: str
    access_token: str
    refresh_token: str
    token_type: str
    expires_in: int


class ErrorResponse(BaseModel):
    status: str
    message: str


class LogoutSuccessResponse(BaseModel):
    status: str
    message: str