import json
#file_name = "data.json"

with open('data.json') as f:
    data = json.load(f)
print(data)
print("Direccion IP:", data["ip"])
print("Sistema operativo:", data["so"])
#print("Versión:", data["version"])
print("Hostname:", data["hostname"])
print("CPU:", data["cpu"])

primer_version = data["version"][0]
print("Versión:", primer_version)