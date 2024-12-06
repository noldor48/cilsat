import sqlite3
from tkinter import *
from tkinter import ttk

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


def pievienot_sasniegumu(perspecid):
    ievade = input("Vai gribat pievienot sasniegumu?(y/n): ")
    if ievade == "y" or ievade == "Y":
        sas_id = int(input("Ievadiet id: "))
        sasniegums = input("Ievadiet sasniegumu: ")
        date = input("Kads datums?: ")
        vieta = input("Kada pilseta?: ")
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

class main():
    root = Tk()
    root.title("Project")
    root.iconbitmap(default="useri.ico")
    root.geometry("300x250")
    root.mainloop()
    while True:
            label0 = ttk.Label()
            label0.pack(anchor=NW, padx=6, pady=6)
            label0["text"] = "1. Pievienot cilveku \n2. Paradit visus cilvekus \n3. Meklet cilveku \n4. Iziet"
            def right():
                print()
            entry = ttk.Entry()
            entry.pack(anchor=NW, padx=6, pady=6)
            
            btn = ttk.Button(text="Click", command=right)
            btn.pack(anchor=NW, padx=6, pady=6)
            
            label1 = ttk.Label()
            label1.pack(anchor=NW, padx=6, pady=6)
            choice = 1
            if choice == '1':add_person()
            elif choice == '2':print_people()
            elif choice == '3':find_person()
            elif choice == '4':
                print("Iziet no programas.")
                break
            else:
                print("Nepareiza izvēle, mēģiniet vēlreiz")
    order_details = cursor.fetchall()
    print("Person details:")
    for detail in order_details:
        print(detail)
    conn.close()
main()