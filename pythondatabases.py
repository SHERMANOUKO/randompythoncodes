import sys
import mysql.connector
from mysql.connector import errorcode

config = {
    'user':'sherman',
    'password':'sherman',
    'host':'127.0.0.1',
    'raise_on_warnings':True
}

tableDescription = (
    "CREATE TABLE `users` ("
    "  `id` bigint(11) NOT NULL AUTO_INCREMENT,"
    "  `name` varchar(50) NOT NULL,"
    "  `phone_number` bigint(11) NOT NULL,"
    "  `user_type` varchar(50) NOT NULL,"
    "  `date_of_birth` datetime NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

insert_data = ("INSERT INTO users "
               "(name, phone_number, user_type, date_of_birth) "
               "VALUES (%s, %s, %s, %s)")

try:
    print("Connecting to Mysql Server")
    cnx = mysql.connector.connect(**config)
    conn = cnx.cursor()
    print("Server Connection Succesfuly Established")
except mysql.connector.Error as err:
    print("Connection to MySQL Server Failed. Outputing Errors...")
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Access Denied Error: "+str(err))
        sys.exit()
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database Does Not Exist: "+str(err))
        sys.exit()
    else:
        print("Error: "+str(err))
        sys.exit()

try:
    print("Establishing Connection To Database If Exists")
    conn.execute("USE mydatabase")
    print("Database Connection Succesful")
except:
    print("Unable to connect to database. Trying to create database.")
    try:
        print("Creating MYDATABASE database")
        conn.execute("CREATE DATABASE IF NOT EXISTS mydatabase DEFAULT CHARACTER SET 'utf8'")
        print("Database Succesfully Created"))
    except mysql.connector.Error as err:
        print("Unable to create Database: "+str(err))
        sys.exit()

try:
    print("Creating table smsdata: ")
    conn.execute(tableDescription)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
        print("Table already exists: "+str(err))
    else:
        print("Error creating table: "+str(err))

try:
    print("inserting user data")
    user_data = ('sherman', '70000001', 'Admin', date(1977, 6, 14))
    conn.execute(insert_data, user_data)
    print("data succesfully inserted")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Access Denied Error: "+str(err))
        sys.exit()
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database Does Not Exist: "+str(err))
        sys.exit()
    else:
        print("Error: "+str(err))
        sys.exit()
        