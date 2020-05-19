import requests
import os
from flask import Flask,render_template,abort
app=Flask(__name__)
#URL BASE
base="https://api.soccersapi.com/v2.2/"
#Variable de Entorno key
key=os.environ["key"]
usuario=os.environ["usuario"]
#Parametros
parametros={'key':key,'user':usuario}

#PAISES
@app.route('/',methods=["GET","POST"])
def inicio():
    r=requests.get(base+'countries/?user=miguelcor.rrss&token=ebb05a4abb67af480efa2a8eadee6ecb&t=list',params=parametros)
    if r.status_code==200:
        doc=r.json()
        paises=[]
        for datos in doc["data"]:
            paises.append(datos)
        return render_template("inicio.html",lista=paises,key=key,usuario=usuario)
    else:
       return "No ha podido ser"
#Equipos
#https://api.soccersapi.com/v2.2/teams/?user=miguelcor.rrss&token=ebb05a4abb67af480efa2a8eadee6ecb&t=list&country_id=3


#Jugadores
#https://api.soccersapi.com/v2.2/players/?user=miguelcor.rrss&token=ebb05a4abb67af480efa2a8eadee6ecb&t=list&country_id=5

#Casas De Apuestas
#https://api.soccersapi.com/v2.2/bookmakers/?user=miguelcor.rrss&token=ebb05a4abb67af480efa2a8eadee6ecb&t=list

#Clasificacion
#https://api.soccersapi.com/v2.2/stats/?user=miguelcor.rrss&token=ebb05a4abb67af480efa2a8eadee6ecb&t=team&id={TEAM_ID}&season_id={SEASON_ID}



app.run(debug=True)