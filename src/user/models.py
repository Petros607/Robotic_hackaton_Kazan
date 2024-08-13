from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    SmallInteger,
    Text
)
from src import models


class User(models.Base):
    __tablename__ = "user"
    metadata = models.metadata

    id = Column(
        "_id",
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True,
    )
    login = Column("_login", String(50), unique=True, nullable=False)
    password_hash = Column("_password_hash", String(128), nullable=False)
    username = Column("_username", String(128), nullable=False)
    email = Column("_email", String(100), nullable=True, unique = True)
    sex = Column("_sex", Boolean, nullable=False)
    age = Column("_age", SmallInteger, nullable=False)
    habitation = Column("_habitation", String(20), default="Казань", nullable=True)
    validation = Column("_validation", Boolean, default=False, nullable=True)
    profession = Column("_profession", String(128), nullable=True)
    address = Column("_address", String(255), nullable=True)
    marriage_status = Column("_marriage_status", Boolean, nullable=True)


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
    refresh_token = Column("_token", Text, unique=True, nullable=False)