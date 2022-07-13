from sqlalchemy.orm import Session

from . import models, schemas

# Category by GetOnBoard ---------------------------------------------
def create_category(db: Session, cat: schemas.GetonboardCategoryCreate):
    db_cat = models.GetonboardCategory(**cat.dict())
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat

def get_categories(db: Session,skip: int = 0, limit: int = 100):
    return db.query(models.GetonboardCategory).offset(skip).limit(limit).all()


# Job -----------------------------------------------------------------

def get_jobs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Job).offset(skip).limit(limit).all()

def get_job(db: Session, plataform: str, plataform_id: str):
    return db.query(models.Job).filter(models.Job.plataform_id == plataform_id and models.Job.plataform == plataform).first()

def create_job(db: Session, jobCreate: schemas.JobCreate):
    db_job = models.Job(**jobCreate.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job


# Usuarios -------------------------------------------------------------

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
