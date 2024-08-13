from fastapi import FastAPI

from src.router import router as router_base
from src.user.router import router as router_user
from src.post.router import router as router_post
from src.comment_estimate.router import router as router_comment
from src.ai.router import router as router_ai

app = FastAPI(
    title="Book of complaints and suggestions of Kazan",
    summary="Книга жалоб и предложений г. Казани",
    description="Проект для участия в хакатоне, проходящий в городе Казань. Прототип сервиса для связи граждан "
                "города Казань с мэрией города для подачи инициатив и поддержания связи между оными по теме инициатив."
                "Выдержан в стиле книг 'Жалоб и предложений'."
)

app.include_router(router_base)
app.include_router(router_user)
app.include_router(router_post)
app.include_router(router_comment)
app.include_router(router_ai)
