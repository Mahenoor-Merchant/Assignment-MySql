import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE if not exists assignment.table1(c1 INT, c2 VARCHAR(255))")

mydb.commit()
mydb.close()