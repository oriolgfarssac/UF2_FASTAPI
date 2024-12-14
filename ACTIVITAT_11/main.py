from fastapi import FastAPI
from dbFunctions import agafarTextBoto, intentsPartida, agafarAbecedari, agafarInfoJugador, comprovarDB

app = FastAPI(debug=True)

#Agafar el text del boto
@app.get("/frase/{idioma_joc}")
def endpointtextboto(idioma_joc: str):
    return {"frase boto" :agafarTextBoto(idioma_joc)}

#Agafar el numero d'intents
@app.post("/partida/{id_partida}/intents")
def endpointintentspartida(id_partida: int):
    return {"numero d'intents": intentsPartida(id_partida)}

#Agafar l'abecedari
@app.get("/abecedari/{idioma}")
def endpointagafarabecedari(idioma: str):
    return {"abecedari": agafarAbecedari(idioma)}

#Agafar la informacio de jugador
@app.get("/jugador/{id_jugador}")
def endpointagafarinfojugador(id_jugador: int):
    infojugador = agafarInfoJugador(id_jugador)

    return {
        "Id_Jugador": id_jugador,
        "Nom_Jugador": infojugador[0],
        "TotalPartides_Jugador": infojugador[1],
        "PartidesGuanyades_Jugador": infojugador[2],
        "PartidesMesPuntsmes_Jugador": infojugador[3],
        "PuntsPartidaActual_Jugador": infojugador[4],
    }

@app.get("/comprovar/")
def comprovarDb():
    return {"comprovar": comprovarDB()}