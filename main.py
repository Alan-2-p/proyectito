import requests
from flask import Flask, jsonify, request
import random
import customtkinter
from customtkinter import *



def cyt():
    lat = 14.63
    lon = -90.55

    url2 = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; Python script)",
        "Accept": "application/json"
    }
    data2 = requests.get(url2, headers=headers).json()

    ll2=[]
    cm = {
    0: "Soleado",
    1: "Mayormente soleado",
    2: "Parcialmente nublado",
    3: "Nublado",
    45: "Niebla",
    48: "Niebla con escarcha",
    51: "Lluvia ligera",
    53: "Lluvia moderada",
    55: "Lluvia intensa",
    56: "Llovizna ligera con escarcha",
    57: "Llovizna intensa con escarcha",
    61: "Chubascos ligeros",
    63: "Chubascos moderados",
    65: "Chubascos intensos",
    66: "Chubascos ligeros con escarcha",
    67: "Chubascos intensos con escarcha",
    71: "Nevada ligera",
    73: "Nevada moderada",
    75: "Nevada intensa",
    77: "Granos de nieve",
    80: "Chubascos aislados",
    81: "Chubascos frecuentes",
    82: "Chubascos muy intensos",
    85: "Chubascos de nieve ligeros",
    86: "Chubascos de nieve intensos",
    95: "Tormenta (posible lluvia)",
    96: "Tormenta con granizo ligero",
    99: "Tormenta con granizo intenso"
}
    for i in data2:
        if type(data2[i]) == dict:

            for j in data2[i]:
                if (j in ["temperature", "windspeed"]):
                    print(f"{j}: {data2[i][j]}")
                    ll2.append(j)
                    ll2.append(data2[i][j])
    cmx= data2["current_weather"]["weathercode"]
    
    l3=CTkLabel(app,text=f"{ll2[0]}: ")
    l4 = CTkLabel(app, text=f"{ll2[2]}: ")
    l5 = CTkLabel(app, text=f"{ll2[5]} {ll2[1]}")
    l6 = CTkLabel(app, text=f"{ll2[7]} {ll2[3]}")
    l15 = CTkLabel(app, text="Clima: ")
    l16 = CTkLabel(app, text=cm[cmx])
    
    l3.grid(column=0, row=5, padx=50, pady=0)
    l4.grid(column=0, row=6, padx=50, pady=0)
    l5.grid(column=1, row=5, padx=50, pady=0)
    l6.grid(column=1, row=6, padx=50, pady=0)
    l15.grid(column=0, row=7, padx=50, pady=0)
    l16.grid(column=1, row=7, padx=50, pady=0)
    
    

app = CTk()
app.title("APIs")
app.geometry("350x300")
app.resizable(width=True,height=True)

cyt()



app.mainloop()