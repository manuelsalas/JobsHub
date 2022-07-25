from xmlrpc.client import boolean
from pydantic import BaseModel

# Categories by GetOnBoard --------------------------------------------
class GetonboardCategoryCreate(BaseModel):
    category: str

class GetonboardCategory(GetonboardCategoryCreate):
    id: int
    class Config:
        orm_mode = True

# Jobs -----------------------------------------------------------------
class JobCreate(BaseModel):
    plataform: str
    plataform_id: str
    title: str
    company: str
    functions: str
    requirements: str
    desirable: str
    seniority: str
    benefits: str
    remote: boolean
    remote_modality: str
    country: str
    category: str

class Job(JobCreate):
    id: int

    class Config:
        orm_mode = True

# Usuario -----------------------------------------------------------------
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
