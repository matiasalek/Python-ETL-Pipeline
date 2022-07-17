# Importo todas las librerias que voy a usar
import pandas as pd
import requests
import airflow

# Guardo el url de la api, params y headers
api_url = 'https://api.yelp.com/v3/businesses/search'
params = {"term": "restaurants",
          "location": "Buenos Aires"}
api_key = "bdGAuRF-OkcKcqikk8RYXv6ii5pAyos8DbWwQhjxkQxeaQA0-RLJtRuMkKKc-d55XeUH6nZls6kJs0Q6Ix" \
          "-4bhpFDpMYugPiVVR7rpX5KswXDZqMHxe602Jxgn7UYnYx "
headers = {"Authorization": "Bearer {}".format(api_key)}

# API requests para conectarme al search engine de Yelp en Buenos Aires
api_get_info_first20 = requests.get(api_url, params=params, headers=headers)

# Con el method json me quedo solo con la data de la api, excluyo la metadata
data_clean = api_get_info_first20.json()

# Otra vez con pandas, esta vez creo un dataframe con la data recibida y limpia de la api
restaurants_buenos_aires_first20 = pd.json_normalize(data_clean["businesses"], sep="_")
params["offset"] = 20
api_get_info_next20 = requests.get(api_url, headers=headers, params=params).json()
restaurants_buenos_aires_next20 = pd.json_normalize(api_get_info_next20["businesses"], sep="_")

restaurants_buenosaires = pd.concat([restaurants_buenos_aires_first20, restaurants_buenos_aires_next20])
print(restaurants_buenosaires.name)
