from fastapi import APIRouter

router = APIRouter(
    tags=["Base"]
)


@router.get("/",
            description="Простая отправка страницы сайта")
@router.get("/home",
            description="Простая отправка страницы сайта")
async def get_home_page():
    return "Home page"


@router.get("/user",
            description="Простая отправка страницы сайта")
async def get_user_page():
    return "User page"


@router.get("/reg",
            description="Простая отправка страницы сайта")
async def get_reg_page():
    return "Registration page"


@router.get("/login",
            description="Простая отправка страницы сайта")
async def get_login_page():
    return "Log in page"


@router.get("/edit-initiative",
            description="Простая отправка страницы сайта")
async def get_edit_initiative_page():
    return "Edit initiative page"


@router.get("/edit-claim",
            description="Простая отправка страницы сайта")
async def get_edit_claim_page():
    return "Edit claim page"


@router.get("/search",
            description="Простая отправка страницы сайта")
async def get_search_page():
    return "Search page"


@router.get("/create",
            description="Простая отправка страницы сайта")
async def get_create_page():
    return "Create page"


@router.get("/object",
            description="Простая отправка страницы сайта")
async def get_object_page():
    return "Object page"
