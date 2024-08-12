from fastapi import APIRouter

router = APIRouter(
    tags=["AI"]
)


@router.get("/questions",
            description="Получение вопросов по тексту")
async def get_questions():
    return "        o(≧▽≦)o"
