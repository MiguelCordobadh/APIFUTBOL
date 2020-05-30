import requests
import os
from flask import Flask,render_template,abort
app=Flask(__name__)
#URL BASE
base="https://api.soccersapi.com/v2.2/"
#Variables de Entorno
key=os.environ["key"]
usuario=os.environ["usuario"]
#INICIO
@app.route('/',methods=["GET","POST"])
def inicio():
    return render_template("inicio.html")

#PAISES
@app.route('/paises',methods=["GET","POST"])
def paises():
    #Parametros
    parametros={'token':key,'user':usuario,'t':"list"}
    r=requests.get(base+'countries/',params=parametros)
    if r.status_code==200:
        doc=r.json()
        continentes=[]
        paises=[]
        for dato in doc["data"]:
            paises.append(dato["name"])
            if dato["continent"] not in continentes:
                continentes.append(dato["continent"])
        return render_template("paises.html",lista=datos,contientes=continentes,paises=paises)
    else:
       return "No ha podido ser"

@app.route('/jugadores/<id>',methods=["GET","POST"])
def jugadores(id):
    parametros={'token':key,'user':usuario,'t':"list",'country_id':id}
    r=requests.get(base+'countries/',params=parametros)
    if r.status_code==200:
        doc=r.json()




#Equipos
#https://api.soccersapi.com/v2.2/teams/?user=miguelcor.rrss&token=ebb05a4abb67af480efa2a8eadee6ecb&t=list&country_id=3


#Jugadores
#https://api.soccersapi.com/v2.2/players/?user=miguelcor.rrss&token=ebb05a4abb67af480efa2a8eadee6ecb&t=list&country_id=5

#Casas De Apuestas
#https://api.soccersapi.com/v2.2/bookmakers/?user=miguelcor.rrss&token=ebb05a4abb67af480efa2a8eadee6ecb&t=list

#Clasificacion
#https://api.soccersapi.com/v2.2/stats/?user=miguelcor.rrss&token=ebb05a4abb67af480efa2a8eadee6ecb&t=team&id={TEAM_ID}&season_id={SEASON_ID}



app.run(debug=True)