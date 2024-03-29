from xml.etree.ElementTree import tostring
import requests
import json
from exec_app import post_jobs


def categories_form_jobs():
    payload={}
    headers = {}

    try:
        url = "http://127.0.0.1/getonboard_categories/"
        response = requests.request("GET", url, headers=headers, data=payload, params = {"page": 1, "size": 5})
        response.raise_for_status()
        r = response.json()

        print(f'Len de cada pagina: {len(r["items"])}')
        print(f'Número elementos: {r["total"]}')
        print(f'Pagina: {r["page"]}')

        for j in range(len(r["items"])):
                print(f'Category {j} : {r["items"][j]["category"]}')

    except requests.exceptions.HTTPError as error:
        print(error)


def jobsbycategories_getonboard():
    payload={}
    headers = {}

    # get a categorias
    # Iterar para cada categoria
    #       get a getonboard jobs e iterar para todas las paginas
    #               post a jobs_app.jobs

    categories = categories_form_jobs()

    for k in range(len(categories["items"])):

        url = 'https://www.getonbrd.com/api/v0/categories/' + categories["items"][j]["category"] + '/jobs?per_page=10&page=' + str(1) + '&expand=["company"]'

        try:
            response = requests.request("GET", url, headers=headers, data=payload)
            response.raise_for_status()
            r = response.json()

            for i in range(r["meta"]["total_pages"]):
                print(f'Len de cada pagina: {len(r["data"])}')
                for j in range(len(r["data"])):
                    print(f'Page {i} Category {j} -- Id : {r["data"][j]["id"]}')
                    categoria = {'category': r["data"][j]["id"]}
                    post_jobs.post_job(categoria)

                url = 'https://www.getonbrd.com/api/v0/categories/' + categories["items"][j]["category"] + '/jobs?per_page=10&page=' + str(i+2) + '&expand=["company"]'

                response = requests.request("GET", url, headers=headers, data=payload)
                response.raise_for_status()
                r = response.json()

        except requests.exceptions.HTTPError as error:
            print(error)


if __name__ == "__main__":
    categories_form_jobs()