import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("UPDATE assignment.costumers SET name = 'ANIME' WHERE costumer_id=654" )
mydb.commit()
mydb.close()