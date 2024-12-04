import flet as ft
import sqlite3

conn = sqlite3.connect('Persons.db')
cursor = conn.cursor()

def add_person():
    print("Jauna persona ar jaunu id")
    id = int(input("Ievadiet id: "))
    firstname = input("Ievadiet vardu: ")
    lastname = input("Ievadiet uzvardu: ")
    birthday = input("Ievadiet birthday: ")
    age = input("Ievadiet vecumu: ")
    gender = input("Ievadiet dzimumu: ")
    email = input("Ievadiet email: ")
    cursor.execute('''INSERT INTO Personas (person_id, firstname, lastname, birthday, age, gender, email)VALUES (?, ?, ?, ?, ?, ?, ?)''', (id, firstname, lastname, birthday, age, gender, email))
    conn.commit()

def print_people():
    cursor.execute("SELECT * FROM Personas")
    orders = cursor.fetchall()
    print("Personas:")
    for order in orders:
        print(order)
    conn.close()

def pievienot_sasniegumu(perspecid):
    ievade = input("Vai gribat pievienot sasniegumu?(y/n): ")
    if ievade == "y" or ievade == "Y":
        sas_id = int(input("Ievadiet id: "))
        sasniegums = input("Ievadiet sasniegumu: ")
        date = input("Kads datums?: ")
        vieta = input("Kada pilseta?: ")
        #person_id = int(input("Ievadiet personas id kurai gribat pievienot sasniegumu: "))
        cursor.execute('''INSERT INTO Sasniegumi (sasnieguma_id, datums, vieta, sasniegums, person_id)VALUES (?, ?, ?, ?, ?)''', (sas_id, date, vieta, sasniegums, perspecid))
        conn.commit()

def find_person():
    perspecid = int(input("Ievadiet personas id kuru meklajat: "))
    cursor.execute("SELECT * FROM Personas")
    orders = cursor.fetchall()
    print("Personas:")
    for order in orders:
        if order[0] == perspecid:
            print(order)
    conn.close()
    pievienot_sasniegumu(perspecid)

def main(page: ft.Page):
    while True:
        page.add(ft.SafeArea(ft.Text("1. Pievienot cilveku")))
        page.add(ft.SafeArea(ft.Text("2. Paradit visus cilvekus")))
        page.add(ft.SafeArea(ft.Text("3. Meklet cilveku")))
        page.add(ft.SafeArea(ft.Text("4. Iziet")))
        choise = input("Izveleties darbibu: ")
        if choise == "1":add_person()          
        elif choise == "2":print_people()
        elif choise == "3":find_person()            
        elif choise == "4":
            break
        else:
            print("Nepareiza darbiba.")

ft.app(main)