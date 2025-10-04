import requests
from flask import Flask, jsonify, request
import random
import customtkinter
from customtkinter import *



def fyh():
    url1 = "https://timeapi.io/api/time/current/zone?timeZone=America%2FGuatemala"
    data = requests.get(url1).json()
    x1 = 0
    x2 = 0
    x3 = 0
    ls=["Año","Mes","Dia","Hora","Minuto"]
    for i in data:
        l1=CTkLabel(app,text=f"{ls[x3]}: ")
        l1.grid(column=0, row=x2, padx=50, pady=0)
        l2 = CTkLabel(app, text=f"{data[i]}")
        l2.grid(column=1, row=x2, padx=50, pady=0)
        x3 = x3 + 1
        x2 = x2 + 1
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

    ll2=[]
    for i in data2:
        if type(data2[i]) == dict:
            print("Guardian Tales")
            for j in data2[i]:
                if (j in ["temperature", "windspeed"]):
                    print(f"{j}: {data2[i][j]}")
                    ll2.append(j)
                    ll2.append(data2[i][j])
    for i in ll2:
        print(i)
    l3=CTkLabel(app,text=f"{ll2[0]}: ")
    l4 = CTkLabel(app, text=f"{ll2[2]}: ")
    l5 = CTkLabel(app, text=f"{ll2[5]} {ll2[1]}")
    l6 = CTkLabel(app, text=f"{ll2[7]} {ll2[3]}")

    l3.grid(column=0, row=5, padx=50, pady=0)
    l4.grid(column=0, row=6, padx=50, pady=0)
    l5.grid(column=1, row=5, padx=50, pady=0)
    l6.grid(column=1, row=6, padx=50, pady=0)




def puchamones():
    
    def mp():
        random_id = random.randint(1, 1025)

        url3 = f"https://pokeapi.co/api/v2/pokemon/{random_id}"
        data3 = requests.get(url3).json()
        url4 = f"https://pokeapi.co/api/v2/pokemon-species/{random_id}"
        data4 = requests.get(url4).json()
        ppp=CTkToplevel()
        ppp.geometry("470x300")
        ppp.attributes("-topmost",True)
        ppp.title("Pokemon")
        ll3=[]
        x4= 6
        l7 = CTkLabel(ppp, text=f"Nombre: {data3['name']}")
        l8 = CTkLabel(ppp, text=f"ID: {data3['id']}")
        l9 = CTkLabel(ppp, text=f"Altura: {data3['height']}")
        l10 = CTkLabel(ppp, text=f"Peso: {data3['weight']}")
        l11 = CTkLabel(ppp, text="Tipos:")
        for i in data3['types']:
            ll3.append(i["type"]["name"])
        
        for i in ll3:
            l12 = CTkLabel(ppp, text=f" - {i}")
            l12.grid(column=0, row=x4, padx=50, pady=0)
            x4 = x4 + 1
        l13 = CTkLabel(ppp, text=f"Generación: {data4['generation']['name'].upper()}")

        for i in data4['flavor_text_entries']:
            if i['language']['name'] == 'es':
                des = i['flavor_text']
                break
        l14 = CTkLabel(ppp, text=f"Descripción: {des}")
        #algunas veces falla la varible des, no se porque
        
        l7.grid(column=0, row=1, padx=50, pady=0)
        l8.grid(column=0, row=2, padx=50, pady=0)
        l9.grid(column=0, row=3, padx=50, pady=0)
        l10.grid(column=0, row=4, padx=50, pady=0)
        l11.grid(column=0, row=5, padx=50, pady=0)
        l13.grid(column=0, row=8, padx=50, pady=0)
        l14.grid(column=0, row=9, padx=50, pady=0)
        
        
    

    bt1=CTkButton(app, command=mp, text="Pokemon")

    
    bt1.grid(column=0, row=7,columnspan=2 ,padx=50, pady=0)
    
    

app = CTk()
app.title("APIs")
app.geometry("350x300")
app.resizable(width=True,height=True)

fyh()
cyt()
puchamones()


app.mainloop()