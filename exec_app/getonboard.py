from xml.etree.ElementTree import tostring
import requests
import json
from exec_app import post_jobs

# API GetOnBoard para cada pagina - categorias en lista json
# llamar API getonboard_category de API Jobs_app
# implementar control de errores


def categories_getonboard():
    payload={}
    headers = {}

    try:
        url = "https://www.getonbrd.com/api/v0/categories?per_page=10&page=1"
        response = requests.request("GET", url, headers=headers, data=payload)
        response.raise_for_status()
        r = response.json()

        for i in range(r["meta"]["total_pages"]):
            print(f'Len de cada pagina: {len(r["data"])}')
            for j in range(len(r["data"])):
                print(f'Page {i} Category {j} -- Id : {r["data"][j]["id"]}')
                categoria = {'category': r["data"][j]["id"]}
                post_jobs.post_job(categoria)

            url = "https://www.getonbrd.com/api/v0/categories?per_page=10&page="+str(i+2)
            response = requests.request("GET", url, headers=headers, data=payload)
            response.raise_for_status()
            r = response.json()

    except requests.exceptions.HTTPError as error:
        print(error)


# ------------------------------------------------------------------------------------
# Jobs from GetOnBoard by Categories
# ------------------------------------------------------------------------------------

def categories_form_jobs():
    payload={}
    headers = {}

    try:
        url = "http://127.0.0.1/getonboard_categories/"
        response = requests.request("GET", url, headers=headers, data=payload, params = {"page": 1, "size": 50})
        response.raise_for_status()
        r = response.json()

        return r["items"]

    except requests.exceptions.HTTPError as error:
        print(error)


def jobsbycategories_getonboard():
    payload={}
    headers = {}

    # get a categorias ok
    # Iterar para cada categoria ok
    #       get a getonboard jobs e iterar para todas las paginas 
    #               completar esquma job desde respuesta
    #               post a jobs_app.jobs

    categories = categories_form_jobs()

    for k in range(len(categories)):

        url = 'https://www.getonbrd.com/api/v0/categories/' + categories[k]["category"] + '/jobs?per_page=10&page=' + str(1) + '&expand=["company"]'

        try:
            response = requests.request("GET", url, headers=headers, data=payload)
            response.raise_for_status()
            r = response.json()

            #print(f'Total de paginas: {r["meta"]["total_pages"]}')
            #print(f'Cantidad de jobs en la pagina: {len(r["data"])}')

            for i in range(r["meta"]["total_pages"]):
                for j in range(len(r["data"])):
                    job = {
                        "plataform": "GetOnBoard",
                        "plataform_id": r["data"][j]["id"],
                        "title": r["data"][j]["attributes"]["title"],
                        "company": r["data"][j]["attributes"]["company"]["data"]["attributes"]["name"],
                        "functions": r["data"][j]["attributes"]["functions"],
                        "requirements": r["data"][j]["attributes"]["description"],
                        "desirable": r["data"][j]["attributes"]["desirable"],
                        "seniority": "",
                        "benefits": str(r["data"][j]["attributes"]["perks"]),
                        "remote": r["data"][j]["attributes"]["remote"],
                        "remote_modality": r["data"][j]["attributes"]["remote_modality"],
                        "country": r["data"][j]["attributes"]["country"],
                        "category": r["data"][j]["attributes"]["category_name"]
                    }
                    post_jobs.post_job(job)

                url = 'https://www.getonbrd.com/api/v0/categories/' + categories[k]["category"] + '/jobs?per_page=10&page=' + str(i+2) + '&expand=["company"]'

                response = requests.request("GET", url, headers=headers, data=payload)
                response.raise_for_status()
                r = response.json()

        except requests.exceptions.HTTPError as error:
            print(error)
