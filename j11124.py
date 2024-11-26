import json

dictionary = []

def add_person():
    id=int(input("Ievadiet id: "))
    firstname = input("Ievadiet vardu: ")
    lastname = input("Ievadiet uzvardu: ")
    birthday = input("Ievadiet birthday: ")
    age = input("Ievadiet vecumu: ")
    gender = input("Ievadiet dzimumu: ")
    email = input("Ievadiet email: ")
    dictionary = {"id":id,
                    "firstname":firstname,
                    "lastname":lastname,
                    "birthday":birthday,
                    "age":age,
                    "gender":gender,
                    "email":email,
                    "sasniegumi":[]}   
    with open('Personas.json', 'r') as openfiles:
        json_objects = json.load(openfiles)    
    json_objects.append(dictionary)
    json_object = json.dumps(json_objects, indent=4)
    with open("Personas.json", "w", encoding="utf-8") as outfile:
        outfile.write(json_object)
    print("Dati ierakstiti faila Personas.json.")

def print_people():
    with open('Personas.json', 'r') as openfile:
        json_object = json.load(openfile)          
    print(json_object)
    
def pievienot_sasniegumu(const):
    while True:
        ievade = input("Vai gribat pievienot sasniegumu?(y/n): ")
        if ievade == "y":
            sasniegums = input("Ievadiet sasniegumu: ")
            date = input("Kads datums?: ")
            vieta = input("Kada pilseta?: ")
            sasniegumss = {
                "datums":date,
                "vieta":vieta,
                "sasniegums":sasniegums
            }
            with open('Personas.json', 'r') as openfiles:
                json_objects = json.load(openfiles)    
            json_objects[const]["sasniegumi"].append(sasniegumss)
            json_object = json.dumps(json_objects, indent=4)
            with open("Personas.json", "w", encoding="utf-8") as outfile:
                outfile.write(json_object)
            print("Dati ierakstiti faila Personas.json.")
        else:
            break

def find_person():
    person_id = int(input("Ievadiet id meklesanai: "))
    with open('Personas.json', 'r') as openfiler:
        json_objekto = json.load(openfiler)
    const = 0
    for i in json_objekto:
        if i["id"] == person_id:
            print("Cilveks atrasts.")            
            pievienot_sasniegumu(const)
            break         
            #dictionary.append(s)
        const += 1


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

main()