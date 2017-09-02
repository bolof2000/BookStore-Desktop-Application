import sqlite3

def connect():
    conn = sqlite3.connect("bolofdb.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS mybook(id INTEGER PRIMARY KEY ,title text,author text,year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn = sqlite3.connect("bolofdb.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO mybook VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("bolofdb.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM mybook")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn = sqlite3.connect("bolofdb.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM mybook WHERE title=? OR author = ? OR year = ? OR isbn=?",(title,author,year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("bolofdb.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM mybook WHERE id = ?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn = sqlite3.connect("bolofdb.db")
    cur = conn.cursor()
    cur.execute("UPDATE mybook SET id = ?,title=?,author=?,year=?,isbn=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()


connect()
insert("The Art of Machine Learning","Adriel Bolofinde",2016,56574444)
print(view())
