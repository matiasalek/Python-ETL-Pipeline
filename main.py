# Importo todas las librerias que voy a usar
import pandas as pd
import requests
import airflow
from pandas.io.json import json_normalize

# Guardo el json que me da una api en una variable url_api
url_api = requests.get('')

# Con pandas leo ese json, con params y headers adecuados
response = pd.read_json(url_api)

# Con el method json me quedo solo con la data de la api, excluyo la metadata
data_clean = response.json()

# Otra vez con pandas, esta vez creo un dataframe con la data recibida y limpia de la api
datafra = pd.DataFrame(data_clean[""])
