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

class main():
    while True:
            print("\n1. Pievienot cilveku")
            print("2. Paradit visus cilvekus")
            print("3. Meklet cilveku")
            print("4. Iziet")
            choice = input("Izveleties darbibu: ")
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