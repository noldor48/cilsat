people = []
while True:
    print("1. Pievienot cilveku")
    print("2. Paradit visus cilvekus")
    print("3. Meklet cilveku")
    print("4. Iziet")
    choise = input("Izveleties darbibu: ")
    if choise == "1":
        print("Jaunas personas izveidosana.")
        firstname = input("Ievadiet vardu: ")
        lastname = input("Ievadiet uzvardu: ")
        email = input("Ievadiet email: ")
        people = people + [firstname]
        file1 = open("person.txt", "a")
        print(str(people))
        file1.write(str(people))
        file1.close()
    elif choise == "2":
        file2 = open("person.txt", "r")
        content = file2.read()
        print(content)
        file2.close()
    elif choise == "3":
        print("Cilveku meklesana.")
        firstname = input("Ievadiet vardu: ")
        file3 = open("person.txt", "r")
        content = file3.read()
        print(content)
        file3.close()
    elif choise == "4":
        break
    else:
        print("Nepareiza darbiba.")
