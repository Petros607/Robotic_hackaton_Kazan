from fastapi import APIRouter

router = APIRouter(
    tags=["User"]
)


@router.post("/register",
             description="Отправка данных о пользователя для регистрации с систему")
async def post_register():
    return "＼(￣▽￣)／"


@router.post("/login",
             description="Отправка данных о пользователя для входа с систему")
async def post_login():
    return "＼(￣▽￣)／"


@router.post("/logout",
             description="Отправка данных о пользователя для выхода из системы")
async def post_logout():
    return "＼(￣▽￣)／"


@router.post("/update_data",
             description="Отправка новых данных о пользователе")
async def post_update_data():
    return "＼(￣▽￣)／"
