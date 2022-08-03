import requests
import json
import sys, os

def post_category(data):
    headers = {}

    try:
        url = "http://127.0.0.1/getonboard_category"
        response = requests.post(url, json=data)
        response.raise_for_status()
        print(response.text)
        data = json.loads(response.text)
        print(data)
        print("Type:", type(data))
        return data

    except requests.exceptions.HTTPError as error:
        print(error)


def post_job(data):
    try:
        url = "http://127.0.0.1/job"
        response = requests.post(url, json=data)
        response.raise_for_status()
        data = json.loads(response.text)
        return data

    except requests.exceptions.HTTPError as error:
        print(error)


if __name__ == "__main__":
    data= {
    'plataform': 'Test-Post Jobs',
    'plataform_id': 'X00---01',
    'title': 'Python Backend',
    'company': 'Kapp',
    'functions': 'Develop API Rest server with FastAPI',
    'requirements': 'Python junior',
    'desirable': 'Web develoment',
    'seniority': 'Junior',
    'benefits': 'competitive salary',
    'remote': 'true',
    'remote_modality': 'fully_remote',
    'country': 'USA',
    'category': 'Prueba'
    }
    post_job(data)