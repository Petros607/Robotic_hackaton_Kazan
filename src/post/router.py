from fastapi import APIRouter

router = APIRouter(
    tags=["Post"]
)


@router.post("/object",
             description="Добавление объекта")
async def post_object():
    return "    ٩(｡•́‿•̀｡)۶"


@router.get("/object/{id_object}",
            description="Получение определенного объекта")
async def get_object(id_object: int):
    return "    ٩(｡•́‿•̀｡)۶"


@router.put("/object/{id_object}",
            description="Изменение определенного объекта")
async def get_object(id_object: int):
    return "    ٩(｡•́‿•̀｡)۶"


@router.delete("/object/{id_object}",
               description="Запрос на удаление определенного объекта")
async def delete_object(id_object: int):
    return "    ٩(｡•́‿•̀｡)۶"


@router.post("/estimate-object/{id_object}",
             description="Добавление оценки на определенный объект")
async def post_estimate(id_object: int):
    return "    ٩(｡•́‿•̀｡)۶"


@router.get("/estimate-object/{id_object}",
            description="Получение оценки на определенный объект")
async def get_estimate(id_object: int):
    return "    ٩(｡•́‿•̀｡)۶"


@router.delete("/estimate-object/{id_object}",
               description="Удаление оценки на определенный объект")
async def delete_estimate(id_object: int):
    return "    ٩(｡•́‿•̀｡)۶"
