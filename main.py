import requests
from flask import Flask, jsonify, request
import random

def fyh():
    url1 = "https://timeapi.io/api/time/current/zone?timeZone=America%2FGuatemala"
    data = requests.get(url1).json()
    x1 = 0
    for i in data:
        print(i, end=": ")
        print(data[i])
        x1 = x1 + 1
        if x1 == 5:
            break

def cyt():
    lat = 14.63
    lon = -90.55

    url2 = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; Python script)",
        "Accept": "application/json"
    }
    data2 = requests.get(url2, headers=headers).json()

    x2 = 0
    for i in data2:
        if type(data2[i]) == dict:
            print("Guardian Tales")
            for j in data2[i]:
                if (j in ["temperature", "windspeed"]):
                    print(f"{j}: {data2[i][j]}")


random_id = random.randint(1, 1025)

# Consulta la API
url3 = f"https://pokeapi.co/api/v2/pokemon/{random_id}"
data3 = requests.get(url3).json()
url4 = f"https://pokeapi.co/api/v2/pokemon-species/{random_id}"
data4 = requests.get(url4).json()

print(f"Nombre: {data3['name']}")
print(f"ID: {data3['id']}")
print(f"Altura: {data3['height']}")
print(f"Peso: {data3['weight']}")
print("Tipos:")
for i in data3['types']:
    print(f" - {i['type']['name']}")
print(f"Generación: {data4['generation']['name'].upper()}")

for i in data4['flavor_text_entries']:
    if i['language']['name'] == 'es':
        des = i['flavor_text']
        break
print(f"Descripción: {des}")
