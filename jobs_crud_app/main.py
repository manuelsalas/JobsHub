from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi_pagination import Page, add_pagination, paginate, Params
from fastapi_crudrouter import MemoryCRUDRouter as CRUDRouter

from . import crud, models, schemas
from .database import SessionLocal, engine

descripcion = """App Test to use the FastAPI Crud extensión"""

app = FastAPI(
    title="Crud App",
    description=descripcion,
    version="0.0.1",
    terms_of_service="http://www.kappcontrol.com",
    contact={
        "name": "Manuel Salas",
        "url": "http://www.kappcontrol.com",
        "email": "manuel.salas@kappcontrol.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },)

# Dependency --
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Crud App"}

# ------------------------------------------------------------------------------------
# CRUD
# ------------------------------------------------------------------------------------

app.include_router(CRUDRouter(schema=schemas.Job, create_schema=schemas.JobCreate, update_schema=schemas.JobUpdate))

