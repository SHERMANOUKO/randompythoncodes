#simple sqlite database connection file for raspberry pi
import sqlite3
from sqlite3 import Error

def createConnection(db_file):
	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print(e)

def createTable(conn, query):
	try:
		c = conn.cursor()
		c.execute(query)
	except Error as e:
		print(e)
	finally:
		conn.close()

query = """CREATE TABLE IF NOT EXISTS data(
		id integer PRIMARY KEY AUTOINCREMENT,
		idno text NOT NULL UNIQUE,
		status int NOT NULL
	);"""

conn = createConnection("data.db")

if conn is not None:
	createTable(conn,query)
else:
	print("Error! Unable to establish database connection")