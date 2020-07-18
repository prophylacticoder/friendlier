import sqlite3

from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('mydatabase.db')
        print("Connection is stablished: database created " +
                "successfully on memory.")
        return con
    except Error:
        print(Error)

def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE messages(id integer PRIMARY KEY, nickname text, message text, datePosted datetime)")

    con.commit()

con = sql_connection()

sql_table(con)
