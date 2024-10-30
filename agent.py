import requests
import pandas as pd
from Levenshtein import distance
from requests.auth import HTTPBasicAuth

API_URL = "http://127.0.0.1:8000/names"
USERNAME = "meu_usuario"
PASSWORD = "minha_senha"

def fetch_names():
    response = requests.get(API_URL, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao obter dados:", response.status_code)
        return []

def analyze_names(names):
    if not names:
        return None

    origin_name = names[0]  
    distances = [(name, distance(origin_name, name)) for name in names[1:]]
    sorted_distances = sorted(distances, key=lambda x: x[1])
    df = pd.DataFrame(sorted_distances, columns=["Nome", "Distância para origem"])
    return df

names = fetch_names()
df = analyze_names(names)

if df is not None:
    print("Referência:", names[0])
    print(df)
else:
    print("Sem dados")
