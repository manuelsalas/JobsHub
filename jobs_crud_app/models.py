from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


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

