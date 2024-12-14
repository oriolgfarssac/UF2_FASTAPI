from connection import conn

def comprovarDB():
    conexio = conn()
    try:
        cur = conexio.cursor()
        cur.execute("USE jocpenjat;")
        cur.execute("SHOW TABLES;")
        tables = cur.fetchall()

        descriptions = {}
        for table in tables:
            table_name = table[0]
            cur.execute(f"DESCRIBE {table_name};")
            descriptions[table_name] = cur.fetchall()

    finally:
        conexio.close()

    return descriptions

def agafarTextBoto(idioma_joc: str):

    conexio = conn()

    try:
        conexio = conn()
        cur = conexio.cursor()
        cur.execute("use jocpenjat;")
        cur.execute("SELECT Frase FROM pantalla WHERE Idioma = %s", (idioma_joc,))

        frase_boto = cur.fetchall()

    finally:
        conexio.close()

    return frase_boto


def intentsPartida(id_partida: int):

    conexio = conn()

    try:
        conexio = conn()

        cur = conexio.cursor()
        cur.execute("use jocpenjat;")
        cur.execute("UPDATE partida SET intents = intents + 1 WHERE partida_id = %s",(id_partida,))
        conexio.commit()

        cur.execute("SELECT intents FROM partida WHERE partida_id = %s", (id_partida,))
        intents_partida = cur.fetchone()

    finally:
        conexio.close()

    return intents_partida


def agafarAbecedari(idioma: str):

    conexio = conn()

    try:
        conexio = conn()
        cur = conexio.cursor()

        cur.execute("use jocpenjat;")
        cur.execute("SELECT Abecedari FROM pantalla WHERE Idioma = %s", (idioma,))
        resultat = cur.fetchone()

        if resultat:
            abecedari = resultat[0]

    finally:
        conexio.close()

    return abecedari


def agafarInfoJugador(id_jugador: int):

    conexio = conn()

    try:
        cur = conexio.cursor()

        cur.execute("use jocpenjat;")
        cur.execute("""SELECT Nom, Total_partides, Partides_ganadas, Partides_mes_punts, Punts_partida_actual FROM jugador WHERE ID = %s """, (id_jugador,))
        resultat = cur.fetchone()

    finally:
        conexio.close()

    return resultat



