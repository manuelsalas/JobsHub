# USA Jobs

from xml.etree.ElementTree import tostring
import requests
import json
from exec_app import post_jobs

# Jobs Category

categories1 = [
    {"Code": "0854","Value": "Computer Engineering"}
]
categories = [
    {"Code": "0854","Value": "Computer Engineering"},
    {"Code": "1550","Value": "Computer Science"},
    {"Code": "1560", "Value": "Data Science Series"},
    {"Code": "1598", "Value": "Mathematics Or Computer Science Trainee"},
    {"Code": "2204", "Value": "CompTechnician"},
    {"Code": "2227", "Value": "Cybersecurity Data Science (For DHS use only)"},
    {"Code": "2226", "Value": "Cybersecurity Risk Man}agement and Compliance (For DHS use only)"},
    {"Code": "2299", "Value": "Information Technology Student Trainee"},
    {"Code": "2210", "Value": "Information Technology Management"},
    {"Code": "2204", "Value": "Computer Technician"},
    {"Code": "1412", "Value": "Technical Information Services"}
]
# ------------------------------------------------------------------------------------
# Jobs from UsaJobs by Categories
# ------------------------------------------------------------------------------------
# https://data.usajobs.gov/api/search?jobcategorycode=1412

def jobs_by_categories():
    payload={}
    headers = {"User-Agent": "m.salas.g@gmail.com", "Authorization-key": "Hbhtu1zrmuPtgdncAoGczYOPEzveSrnbOBO7/OFst84=" }
    url_base = 'https://data.usajobs.gov/api/search?jobcategorycode='

    for k in range(len(categories)):
        try:
            url = url_base + categories[k]["Code"]+'&Page=' + str(1)
            response = requests.request("GET", url, headers=headers, data=payload)
            response.raise_for_status()
            r = response.json()

            pages = int(r["SearchResult"]["UserArea"]["NumberOfPages"])

            for i in range(pages):
                url = url_base + categories[k]["Code"]+'&Page=' + str(i+1)
                response = requests.request("GET", url, headers=headers, data=payload)
                response.raise_for_status()
                r = response.json()

                for j in range(int(r["SearchResult"]["SearchResultCount"])):

                    id = r["SearchResult"]["SearchResultItems"][j]["MatchedObjectDescriptor"]["PositionID"]
                    cat = categories[k]["Code"]
                    print(f'Categoria ({cat}) ID = {id} - i = {i} - j = {j}')

                    job = {
                        "plataform": "USAJobs",
                        "plataform_id": r["SearchResult"]["SearchResultItems"][j]["MatchedObjectDescriptor"]["PositionID"],
                        "title": r["SearchResult"]["SearchResultItems"][j]["MatchedObjectDescriptor"]["PositionTitle"],
                        "company": r["SearchResult"]["SearchResultItems"][j]["MatchedObjectDescriptor"]["OrganizationName"],
                        "functions": str(r["SearchResult"]["SearchResultItems"][j]["MatchedObjectDescriptor"]["UserArea"]["Details"]["MajorDuties"][0]),
                        "requirements": r["SearchResult"]["SearchResultItems"][j]["MatchedObjectDescriptor"]["UserArea"]["Details"]["Education"],
                        "desirable": "",
                        "seniority": "",
                        "benefits": "",
                        "remote": "true",
                        "remote_modality": "",
                        "country": r["SearchResult"]["SearchResultItems"][j]["MatchedObjectDescriptor"]["PositionLocationDisplay"],
                        "category": r["SearchResult"]["SearchResultItems"][j]["MatchedObjectDescriptor"]["JobCategory"][0]["Name"]
                    }
                    post_jobs.post_job(job)

        except requests.exceptions.HTTPError as error:
            print(error)

if __name__ == "__main__":
    jobs_by_categories()