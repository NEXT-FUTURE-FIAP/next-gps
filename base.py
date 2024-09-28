import requests
import folium

LatitudeURL = "http://3.141.30.96:1026/v2/entities/urn:ngsi-ld:next_gps/attrs/Latitude"
LongitudeURL = "http://3.141.30.96:1026/v2/entities/urn:ngsi-ld:next_gps/attrs/Longitude"


payload = ""
headers = {
  'fiware-service': 'smart',
  'fiware-servicepath': '/',
  'accept': 'application/json'
}

LatitudeRequest = requests.request("GET", LatitudeURL, headers=headers, data=payload)
LongitudeRequest = requests.request("GET", LongitudeURL, headers=headers, data=payload)



# Coordenadas da localização
# Coordenadas da localização
latitude = LatitudeRequest.json()["value"]
longitude = LongitudeRequest.json()["value"]


# Cria o mapa
mapa = folium.Map(location=[latitude, longitude], zoom_start=15)

# Adiciona um marcador
folium.Marker([latitude, longitude], popup='Localização').add_to(mapa)

# Salva o mapa em um arquivo HTML
mapa.save('mapa.html')

print("Mapa gerado: mapa.html")