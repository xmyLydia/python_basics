import mysql.connector

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)
cursor = con.cursor()

word = input("Enter a word: ")
query = cursor.execute("select * from Dictionary where Expressionr = '%s'" % word)
results = cursor.fetchall()
if results:
    for result in results:
        print(result)
else:
    print("Word not found")