# Importo todas las librerias que voy a usar
import pandas as pd
import requests
import airflow
from pandas.io.json import json_normalize

# Guardo el url de la api, params y headers
api_url = 'https://api.yelp.com/v3/businesses/search'
params = {"term": "restaurants",
          "location": "Buenos Aires"}
api_key = # API Key la mantengo privada
headers = {"Authorization": "Bearer {}".format(api_key)}

# Guardo el json que me da una api en una variable url_api
api_get_info = requests.get(api_url, params=params, headers=headers)

# Con pandas leo ese json, con params y headers adecuados
response = pd.read_json(api_get_info)

# Con el method json me quedo solo con la data de la api, excluyo la metadata
data_clean = response.json()

# Otra vez con pandas, esta vez creo un dataframe con la data recibida y limpia de la api
datafra = pd.DataFrame(data_clean[""])
