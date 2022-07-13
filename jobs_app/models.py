from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class GetonboardCategory(Base):
    __tablename__ = "getonboard_category"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, unique=True, index=True)


class Job(Base):
    __tablename__ = "job"

    id = Column(Integer, primary_key=True, index=True)
    plataform = Column(String, index=True)
    plataform_id = Column(String, unique=True, index=True)
    title = Column(String, index=True)
    company = Column(String, index=True)
    functions = Column(String)
    requirements = Column(String)
    desirable = Column(String)
    seniority = Column(String)
    benefits = Column(String)
    remote = Column(Boolean)
    remote_modality = Column(String)
    country = Column(String, index=True)
    category = Column(String, index=True)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
