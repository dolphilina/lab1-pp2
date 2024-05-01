import psycopg2
import csv

conn = psycopg2.connect(
    host = 'localhost',
    dbname = 'Lab10',
    user = 'postgres',
    password = '260106'
)

cur = conn.cursor()

def inputData():
    name = input("Hello input your name: ")
    number = input("Input your phone number: ")
    cur.execute(' INSERT INTO phone_book("name", "number") VALUES( %s, %s); ' , (name, number))

def importFromCSV():
    path = input("Enter path to csv file: ")
    with open(path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            personName, phoneNumber = row
            cur.execute(' INSERT INTO phone_book("name", "number") VALUES( %s, %s); ', (personName, phoneNumber))


def update_contact(personName, phoneNumber):
    cur.execute(' UPDATE phone_book SET "number" = %s WHERE "name" = %s ', (phoneNumber, personName))

def queryData():
    cur.execute(' SELECT * FROM phone_book ')
    data = cur.fetchall()
    path = r"C:\\Users\\user\\Documents\\GitHub\\lab1-pp2\\W10\\phonebook\\data.txt"

    f = open(path, "w")
    
    i=0
    for row in data:
        i += 1
        f.write(str(i) + "." + "\n" + "Name: " + str(row[0]) + "\n" + "Number: " + str(row[1]) + "\n")
    f.close()

def deleteData():
    print("Which name do ypu want to delete?\n")
    personName = input()
    cur.execute(f''' DELETE FROM phone_book WHERE "name"='{personName}' ''')

def deleteAllData():
    cur.execute(' DELETE FROM phone_book ')

done = False
while not done:
    print("What do you want to do?\n\
          1. Input data from console\n\
          2. Upload form csv file\n\
          3. Update existing contact\n\
          4. Query data from the table\n\
          5. Delete data from table by person name\n\
          6. Delete all data from table\n\
          7. Exit")
    x = int(input("Enter number 1-7\n"))
    if(x == 1):
        inputData()
    elif(x == 2):
        importFromCSV()
    elif(x == 3):
        print("Which number do you want to update? Enter name and new number: ")
        name = input()
        newNumber = input()
        update_contact(name, newNumber)
    elif(x == 4):
        queryData()
    elif(x == 5):
        deleteData()
    elif(x == 6):
        deleteAllData()
    elif(x == 7):
        done = True
    conn.commit()
    
cur.close()
conn.close()