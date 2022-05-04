import mysql.connector

db = mysql.connector.connect(
    host='localhost', user='test', password='test', database='test'
)
cursor = db.cursor()

course = input("Give course: ")

query = "INSERT INTO courses (title, level) VALUES ('" + course + "', '2')"
cursor.execute(query)
db.commit()

query = "SELECT * FROM courses"

cursor.execute(query)

data = cursor.fetchall()

for row in data:
    print(row[1])

