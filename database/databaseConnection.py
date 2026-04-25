import mysql.connector as SQLC
# login to database
database_config = SQLC.connect(
    host = "localhost",
    user = "root",
    password = 'Rishikesh#2003',
    database = "atm_db"

)
# creating cursor object
cursor = database_config.cursor()
# print(cursor,database_config)