from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    ForeignKey,
    Text
)
from src import models


class Token(models.Base):
    __tablename__ = "token"
    metadata = models.metadata
    id = Column(
        "_id",
        Integer,
        unique=True,
        autoincrement=True,
        primary_key=True,
        nullable=False,
    )
    user_id = Column(
        "_user_id", Integer, ForeignKey("user._id"), unique=False, nullable=False
    )
    referesh_token = Column("_token", Text, unique=True, nullable=False)
