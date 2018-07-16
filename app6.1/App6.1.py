import psycopg2


def create_connection(string):
    conn = psycopg2.connect(string)
    return conn


def create_table(conn):
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    return 0


def insert(conn, item, quantity, price):
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))
    return 0


def view(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    return rows


def delete(conn, item):
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    return 0


def update(conn, quantity, price, item):
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
    return 0


if __name__ == "__main__":
    sql_connection = create_connection("dbname='mydb' user='postgres' password='root' host='127.0.0.1' port='5432'")
    create_table(sql_connection)
    insert(sql_connection, "apple", 6, 2.75)
    sql_connection.commit()
    print(view(sql_connection))
    sql_connection.close()