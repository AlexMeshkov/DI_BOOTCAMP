import psycopg2

connection = psycopg2.connect(
    database="avecoder",
    user="postgres",
    password="root",
    host="localhost",
    port="5432",
)


def retrive_actors_numberoscars():
    try:
        with connection:
            with connection.cursor() as curs:
                query = "SELECT * FROM actors"
                curs.execute(query)
                data = curs.fetchall()
                print(data)

    except Exception as err:
        print(err)


retrive_actors_numberoscars()

connection.close()


def retrive_actors_cars(lastname):
    try:
        with connection:
            with connection.cursor() as curs:
                query = f"""
                SELECT first_name, brand, type
                FROM actor
                INNER JOIN car ON actor.id = car.owner_id
                WHERE last_name = {lastname}
                """
                curs.execute(query)
                data = curs.fetchall()
                print(data)
    except Exception as err:
        print(err)


retrive_actors_cars("Clooney")

connection.close
