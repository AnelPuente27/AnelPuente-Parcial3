import requests

url = "https://api.thecatapi.com/v1/images/search?limit=10" 
response = requests.get(url)

if response.status_code == 200:
   data = response.json()
   print('Solicitud exitosa')
   print("Datos:", data)
else:
   print("Error en la solicitud: ", response.text)