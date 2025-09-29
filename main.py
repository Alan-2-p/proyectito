import requests
from flask import Flask, jsonify, request

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
    print(i, end=": ")
    print(data2[i])
    x2 = x2 + 1

