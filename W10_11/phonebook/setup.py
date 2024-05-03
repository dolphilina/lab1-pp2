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
    cur.execute(' SELECT * FROM phone_book ')
    data = cur.fetchall()
    for row in data:
        if(name == str(row[0])):
            print("Name already exist. Contact is updated.")
            update_contact(name, number)
        else: 
            print("Contact is added.")
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

def queryData(limit, offset):
    cur.execute('SELECT * FROM phone_book LIMIT %s OFFSET %s', (limit, offset))
    data = cur.fetchall()
    path = r"C:\\Users\\user\\Documents\\GitHub\\lab1-pp2\\W10_11\\phonebook\\data.txt"

    f = open(path, "w")
    
    i = offset
    for row in data:
        i += 1
        f.write(str(i) + "." + "\n" + "Name: " + str(row[0]) + "\n" + "Number: " + str(row[1]) + "\n")
    f.close()
    
def queryByPattern(pattern):
    print("How do you want to search?\n\
          1. By name\n\
          2. By number\n\
            ")
    y = int(input("Enter number 1-2\n"))
    if(y == 1):
        cur.execute('SELECT * FROM phone_book WHERE "name" LIKE %s', ('%' + pattern + '%',))
        data = cur.fetchall()
        path = r"C:\\Users\\user\\Documents\\GitHub\\lab1-pp2\\W10_11\\phonebook\\data.txt"
    elif(y == 2):
        cur.execute('SELECT * FROM phone_book WHERE "number" LIKE %s', ('%' + pattern + '%',))
        data = cur.fetchall()
        path = r"C:\\Users\\user\\Documents\\GitHub\\lab1-pp2\\W10_11\\phonebook\\data.txt"

    f = open(path, "w")
    
    i=0
    for row in data:
        i += 1
        f.write(str(i) + "." + "\n" + "Name: " + str(row[0]) + "\n" + "Number: " + str(row[1]) + "\n")
    f.close()

def deleteData():
    print("How do you want to delete?\n\
          1. By name\n\
          2. By number\n\
            ")
    y = int(input("Enter number 1-2\n"))
    if(y == 1): 
        print("Which name do you want to delete?\n")
        personName = input()
        cur.execute(f''' DELETE FROM phone_book WHERE "name"='{personName}' ''')
    elif(y == 2): 
        print("Which number do you want to delete?\n")
        personNum = input()
        cur.execute(f''' DELETE FROM phone_book WHERE "name"='{personNum}' ''')

def deleteAllData():
    cur.execute(' DELETE FROM phone_book ')

done = False
while not done:
    print("What do you want to do?\n\
          1. Input data from console\n\
          2. Upload from CSV file\n\
          3. Update existing contact\n\
          4. Query data from the table\n\
          5. Query data by pattern\n\
          6. Delete data from table by person name\n\
          7. Delete all data from table\n\
          8. Exit")
    x = int(input("Enter number 1-8\n"))
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
        limit = int(input("Enter limit: "))
        offset = int(input("Enter offset: "))
        queryData(limit, offset)
    elif x == 5:
        pattern = input("Enter the pattern to search: ")
        queryByPattern(pattern)
    elif(x == 6):
        deleteData()
    elif(x == 7):
        deleteAllData()
    elif(x == 8):
        done = True
    conn.commit()
    
cur.close()
conn.close()