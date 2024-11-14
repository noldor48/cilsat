import json

personasss = []
def pievienot_cilveku():
    firstname = input("Ievadiet vardu: ")
    lastname = input("Ievadiet uzvardu: ")
    birthday = input("Ievadiet birthday: ")
    age = input("Ievadiet vecumu: ")
    gender = input("Ievadiet dzimumu: ")
    email = input("Ievadiet email: ")
    dictionary = {"firstname":firstname,
                    "lastname":lastname,
                    "birthday":birthday,
                    "age":age,
                    "gender":gender,
                    "email":email}
    file = open('Personas.json', 'r')
    data=json.load(file)
    file.close()
    json_object = json.dumps(dictionary, indent=4)
    with open("Personas.json", "w", encoding="utf-8") as outfile:
        outfile.write(json_object)
    print("Dati ierakstiti faila Personas.json.")

def paradit_cilvekus():
    with open('Personas.json', 'r') as openfile:
        json_object = json.load(openfile)           
    print(json_object)

class main():
    while True:
            print("\n1. Pievienot cilveku")
            print("2. Paradit visus cilvekus")
            print("3. Meklet cilveku")
            print("4. Iziet")
            choice = input("Izveleties darbibu: ")

            if choice == '1':
                pievienot_cilveku()
            elif choice == '2':
                paradit_cilvekus()
            elif choice == '3':
                paradit_cilvekus()
            elif choice == '4':
                print("Iziet no programas.")
                break
            else:
                print("Nepareiza izvēle, mēģiniet vēlreiz")

main()






'''with open('Personas.json', 'r') as openfile:
        json_object = json.load(openfile)           
    print(json_object)
    dictator = dictionary
    dictator.update(json_object)'''