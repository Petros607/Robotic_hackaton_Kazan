from fastapi import APIRouter

router = APIRouter(
    tags=["Comment and estimate"]
)


@router.post("/estimate-comment",
             description="Запрос на добавление оценки к комментарию")
async def post_estimate_comment():
    return "    ＼(≧▽≦)／"


@router.delete("/estimate-comment/{id_estimate_comment}",
               description="Отменить оценку определенного комментария")
async def delete_estimate_comment(id_estimate_comment: int):
    return "    ＼(≧▽≦)／"


@router.post("/comment",
             description="Запрос на добавление комментария")
async def post_comment():
    return "    ＼(≧▽≦)／"


@router.delete("/comment/{id_comment}",
               description="Запрос на удаление определенного комментария")
async def delete_comment(id_comment: int):
    return "    ＼(≧▽≦)／"


@router.post("/comment/{id_comment}/edit",
             description="Запрос на редактирование определенного комментария")
async def post_estimate_comment(id_comment: int):
    return "    ＼(≧▽≦)／"
