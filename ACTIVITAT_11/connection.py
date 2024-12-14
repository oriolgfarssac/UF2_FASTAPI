import mysql.connector
from mysql.connector import Error

def conn():
    try:
        dbname = "jocpenjat"
        user = "root"
        password = "root"
        host = "localhost"
        port = 3306
        collation = "utf8mb4_general_ci"

        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=dbname,
            collation=collation
        )

        if connection.is_connected():
            print(f"T'has connectat a la base de dades '{dbname}' !")
            return connection

    except Error as e:
        print(f"Error en connectar-te a la base de dades: {e}")

    return None
