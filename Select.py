import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("select * from ASSIGNMENT.COSTUMERS")
for i in mycursor.fetchall():
  print(i)

mydb.close()