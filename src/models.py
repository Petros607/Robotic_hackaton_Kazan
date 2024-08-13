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
    Enum,
    SmallInteger,
)
from sqlalchemy import MetaData
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import DeclarativeBase

from src.enums import (
    ObjectTypeEnum,
    ObjectStatusEnum,
    EstimateEnum,
    DecisionConclusionEnum,
)

metadata = MetaData()


class Base(DeclarativeBase):
    metadata = metadata
    pass


class AbstractObject(Base):
    __tablename__ = "abstract_object"
    metadata = metadata

    id = Column(
        "_id",
        Integer,
        unique=True,
        nullable=False,
        autoincrement=True,
        primary_key=True,
    )
    object_type = Column(
        "_type",
        Enum(ObjectTypeEnum, name="object_type_enum"),
        unique=False,
        autoincrement=False,
        nullable=False,
    )
    title = Column("_title", String(100), unique=False, nullable=False)
    text = Column("_text", Text, nullable=False)
    status = Column(
        "_status", Enum(ObjectStatusEnum, name="status_enum"), nullable=True
    )
    images = Column("_images", ARRAY(String(128)), nullable=True)
    docs = Column("_docs", ARRAY(String(128)), nullable=True)
    decision = Column("_decision", Integer, ForeignKey("decision._id", name = "abstract_object__decision_fkey"), nullable=True)
    utility_rating = Column("_utility_rating", Integer, default=0)
    relevance_rating = Column("_relevance_rating", Float, default=0)
    relevance_rating_day = Column("_relevance_rating_day", Float, default=0)
    count_subscribers = Column("_count_subscribers", Integer, default=0)
    datetime_creation = Column("_datetime_creation", DateTime, nullable=False)
    datetime_edit = Column("_datetime_edit", DateTime, nullable=True)


class Decision(Base):
    __tablename__ = "decision"
    metadata = metadata

    id = Column("_id", Integer, unique=True, primary_key=True, autoincrement=True)
    text = Column("_text", Text, nullable=False)
    conclusion = Column(
        "_conclusion",
        Enum(DecisionConclusionEnum, name="conclusion_enum"),
        nullable=False,
    )
    object_id = Column(
        "_object_id", Integer, ForeignKey("abstract_object._id", name = "decision__object_id_fkey"), nullable=False
    )
    datetime_creation = Column("_datetime_creation", DateTime, nullable=False)


class Comment(Base):
    __tablename__ = "comment"
    metadata = metadata

    id = Column("_id", Integer, unique=True, primary_key=True, autoincrement=True)
    user_id = Column("_user_id", Integer, ForeignKey("user._id"), nullable=False)
    object_id = Column(
        "_object_id", Integer, ForeignKey("abstract_object._id"), nullable=False
    )
    text = Column("_text", Text, nullable=False)
    rating = Column("_rating", Integer)


class CommentEstimate(Base):
    __tablename__ = "comment_estimate"
    metadata = metadata

    id = Column("_id", Integer, unique=True, primary_key=True, autoincrement=True)
    estimation = Column(
        "_estimation", Enum(EstimateEnum, name="estimate_enum"), nullable=False
    )
    user_id = Column("_user_id", Integer, ForeignKey("user._id"), nullable=False)
    comment_id = Column(
        "_comment_id", Integer, ForeignKey("comment._id"), nullable=False
    )


class Subscribe(Base):
    __tablename__ = "subscribe"
    metadata = metadata

    id = Column("_id", Integer, unique=True, primary_key=True, autoincrement=True)
    user_id = Column("_user_id", Integer, ForeignKey("user._id"), nullable=False)
    object_id = Column(
        "_object_id", Integer, ForeignKey("abstract_object._id"), nullable=False
    )


class ObjectEstimate(Base):
    __tablename__ = "object_estimate"
    metadata = metadata

    id = Column("_id", Integer, unique=True, primary_key=True, autoincrement=True)
    user_id = Column("_user_id", Integer, ForeignKey("user._id"), nullable=False)
    object_id = Column(
        "_object_id", Integer, ForeignKey("abstract_object._id"), nullable=False
    )
    datetime = Column("_datetime", DateTime, nullable=False)
    rating = Column("_rating", Enum(EstimateEnum, name="estimate_enum"), nullable=False)
