from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi_pagination import Page, add_pagination, paginate, Params

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

descripcion = """Recopila las ofertas laborales publicadas en las siguientes plataformas: GetOnBoard, Indeed y Linkedin."""

app = FastAPI(
    title="Jobs App",
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
    return {"message": "Jobs App"}


# ------------------------------------------------------------------------------------
# Categories by GetOnBoard
# ------------------------------------------------------------------------------------

@app.post("/getonboard_category/", response_model=schemas.GetonboardCategory)
def create_getonboard_category(
    cat: schemas.GetonboardCategoryCreate, db: Session = Depends(get_db)):
    db_cat = crud.get_category(db, category=cat.category)
    if db_cat is not None:
        raise HTTPException(status_code=400, detail="Category already registered")
    return crud.create_category(db=db, cat=cat)

@app.get("/getonboard_categories/", response_model=Page[schemas.GetonboardCategory])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), params: Params = Depends()):
    categories = crud.get_categories(db, skip=skip, limit=limit)
    return paginate(categories, params)

#add_pagination(app)


# ------------------------------------------------------------------------------------
# Jobs
# ------------------------------------------------------------------------------------

@app.post("/job/", response_model=schemas.Job)
def create_job_by_plataform(
    jobCreate: schemas.JobCreate, db: Session = Depends(get_db)):
    db_job = crud.get_job(db, plataform = jobCreate.plataform, plataform_id=jobCreate.plataform_id)
    if db_job is not None:
        raise HTTPException(status_code=400, detail="Job already registered")
    return crud.create_job(db=db, jobCreate=jobCreate)



# ------------------------------------------------------------------------------------
# Usuarios
# ------------------------------------------------------------------------------------

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user is not None:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is not None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user



