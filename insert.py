import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("INSERT INTO assignment.costumers (name, costumer_id, email_id) VALUES ('SURESH', 654, 'suresh@gmail.com')")
mycursor.execute("INSERT INTO assignment.costumers (name, costumer_id, email_id) VALUES ('HARRY', 981, 'harrypotter@gmail.com')")

mydb.commit()
mydb.close()
