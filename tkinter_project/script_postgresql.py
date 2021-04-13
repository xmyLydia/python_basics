import psycopg2
from database_credentials import user
from database_credentials import password


def create_table():
    connect_str = "dbname='database_exercise' user=%s password=%s host='localhost' port='5432'" % (user,
                                                                                                   password)
    conn = psycopg2.connect(connect_str)
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    connect_str = "dbname='database_exercise' user=%s password=%s host='localhost' port='5432'" % (user,
                                                                                                   password)
    conn = psycopg2.connect(connect_str)
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s, %s, %s)",
                (item, quantity, price))
    conn.commit()
    conn.close()


def delete(item):
    connect_str = "dbname='database_exercise' user=%s password=%s host='localhost' port='5432'" % (user,
                                                                                                   password)
    conn = psycopg2.connect(connect_str)
    cur = conn.cursor()
    cur.execute("DELETE FROM store where item=%s", (item,))
    conn.commit()
    conn.close()


def update(item, quantity, price):
    connect_str = "dbname='database_exercise' user=%s password=%s host='localhost' port='5432'" % (user,
                                                                                                   password)
    conn = psycopg2.connect(connect_str)
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",
                (quantity, price, item))
    conn.commit()
    conn.close()


def view():
    connect_str = "dbname='database_exercise' user=%s password=%s host='localhost' port='5432'" % (user,
                                                                                                   password)
    conn = psycopg2.connect(connect_str)
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()


#update("Orange", 10, 10)
view()
#conn = psycopg2.connect("lite.db")
#update("BOOK1", 10, 10)
#delete("another book")
# view(conn)
