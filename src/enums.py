import enum


class ObjectTypeEnum(enum.Enum):
    INITIATIVE = "Инициатива"
    CLAIM = "Жалоба"
    PROJECT = "Проект"


class ObjectStatusEnum(enum.Enum):
    CLOSED = "Закрыто"
    FROZEN = "Заморожено"
    ACTIVE = "Активно"


class DecisionConclusionEnum(enum.Enum):
    APPROVED = "Одобрено"
    REJECTED = "Отклонено"
    FROZEN = "Заморожено"


class EstimateEnum(enum.Enum):
    LIKE = 1
    DISLIKE = -1

# TODO: дописать  типы статусов
