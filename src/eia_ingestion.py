import requests
from dotenv import load_dotenv
import os 
from pathlib import Path

env_path= Path(__file__).resolve().parent.parent/".env"
load_dotenv(env_path)

API_KEY = os.getenv("EIA_API_KEY")


url = 'https://api.eia.gov/v2/electricity/rto/daily-fuel-type-data/data/'

params = {
    "api_key" : API_KEY,
    "frequency": "daily",
    "data[0]": "value",
    "start": "2026-08-08",
    "end": "2026-08-08",
    "offset":0,
    "length": 5000
}

response = requests.get(url, params=params) ## (Haz una petición GET a esta url, utilizando estos params.)  

print(response.status_code)

data = response.json()

with open("eia_response.json","w") as file:
        import json
        json.dump(data, file, indent=2)

