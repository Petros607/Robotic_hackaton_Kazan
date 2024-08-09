from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    ForeignKey,
    Text,
    Boolean,
    Float,
    DateTime,
)
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(
        "_id",
        String(64),
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True,
    )
    username = Column("_username", String(128), nullable=False)
    email = Column("_email", String(100), nullable=True)
    sex = Column("_sex", Boolean, nullable=False)
    age = Column("_age", Integer, unsigned=True, nullable=False)
    habitation = Column("_habitation", String(20), default="Казань", nullable=True)
    validation = Column("_validation", Boolean, default=False)
    profession = Column("_profession", String(128), nullable=True)
    address = Column("_address", String(255))
    marriage_status = Column("_marriage_status", Boolean, nullable=True)


class AbstractObject(Base):
    __tablename__ = "abstract_object"
    id = Column(
        "_id",
        Integer,
        unique=True,
        nullable=False,
        autoincrement=True,
        primary_key=True,
    )
    object_type = Column(
        "_type", Integer, unique=False, autoincrement=False, nullable=False
    )
    title = Column("_title", String(100), unique=False, nullable=False)
    text = Column("_text", Text, nullable=False)
    status = Column("_status", String(50), nullable=True)
    images = Column("_images", ARRAY(String(128)), nullable=True)
    docs = Column("_docs", ARRAY[String(128)], nullable=True)
    decision = Column("_decision", Integer, ForeignKey("decision._id"))
    utility_rating = Column("_utility_rating", Integer, default=0)
    relevance_rating = Column("_relevance_rating", Float, default=0)
    relevance_rating_day = Column("_relevance_rating_day", Float, default=0)
    count_subscribers = Column("_count_subscribers", Integer, default=0)
    datetime_creation = Column("_datetime_creation", DateTime, nullable=False)
    datetime_edit = Column("_datetime_edit", DateTime, nullable=True)


class Decision(Base):
    __tablename__ = "decision"
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
