from database import connection
import psycopg2


def read_table():

        conn = connection()
        cursor = conn.cursor()

        cursor.execute("select * from USERS")

        registers = cursor.fetchall()

        users = []

        for register in registers:

            user_dict = {
                "id": register[0],
                "name": register[1],
                "email": register[2],
            }

            users.append(user_dict)

        if conn:
            conn.close()

        return users
