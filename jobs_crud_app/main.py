from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi_pagination import Page, add_pagination, paginate, Params
from fastapi_crudrouter import MemoryCRUDRouter as CRUDRouter
from fastapi_crudrouter import SQLAlchemyCRUDRouter

from . import schemas, models, database
from .database import SessionLocal, engine

descripcion = """App Test to use the FastAPI Crud extension
Tired of rewriting the same generic CRUD routes? Need to rapidly prototype a feature for a presentation or a hackathon? Thankfully, fastapi-crudrouter has your back. As an extension to the APIRouter included with FastAPI, the FastAPI CRUDRouter will automatically generate and document your CRUD routes for you, all you have to do is pass your model and maybe your database connection.
FastAPI-CRUDRouter is also lightning fast, well tested, and production ready."""

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
        db.commit()
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Crud App"}

# ------------------------------------------------------------------------------------
# CRUD
# ------------------------------------------------------------------------------------

router = SQLAlchemyCRUDRouter(
    schema=schemas.Job,
    create_schema=schemas.JobCreate,
    update_schema=schemas.JobUpdate,
    db_model=models.Job,
    db=get_db,
    prefix='job'
)

app.include_router(router)