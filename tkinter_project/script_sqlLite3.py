import sqlite3


def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()



def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store where item=?", (item,))
    conn.commit()
    conn.close()


def update(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",
                (quantity, price, item))
    conn.commit()
    conn.close()


def view(conn):
   
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    for row in rows:
        print(row)

conn = sqlite3.connect("lite.db")
update("BOOK1", 10, 10)
#delete("another book")
view(conn)
