from xmlrpc.client import boolean
from pydantic import BaseModel

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

class JobUpdate(BaseModel):
    #plataform: str
    #plataform_id: str
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
