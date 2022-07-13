from fastapi import Depends, FastAPI, HTTPException
from jobs_app import crud, models, schemas
from exec_app import getonboard, post_jobs


descripcion = """Consume las ofertas laborales publicadas en las API Publicas siguientes plataformas: 
                   - GetOnBoard
                   - Indeed
                   - Linkedin

                Con las respuestas se consume las API de Jobs_app para insertar las ofertas
                en la BD jobs_app en PostgreSQL.
                   """

app = FastAPI(
    title="Exec App",
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



@app.get("/")
def root():
    return {"message": "Exec App - Platform Jobs API Consume"}


# ------------------------------------------------------------------------------------
# GetOnBoard - Categories
# ------------------------------------------------------------------------------------

@app.get("/UpGetOnBoardCategories/", response_model=schemas.GetonboardCategory)
def SaveCategories(skip: int = 0, limit: int = 100):
   return getonboard.categories_getonboard()

# ------------------------------------------------------------------------------------
# GetOnBoard - Jobs x Category
# ------------------------------------------------------------------------------------

@app.get("/UpGetOnBoardJobsbyCategories/", response_model=schemas.Job)
def SaveJobsbyCategories(skip: int = 0, limit: int = 100):
   return getonboard.jobsbycategories_getonboard()




