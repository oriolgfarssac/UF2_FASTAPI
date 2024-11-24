import psycopg2


def connection():
    conn = psycopg2.connect(
        database="mydatabase",
        user="root",
        password="root",
        host="localhost",
        port="5432"
    )
    return conn