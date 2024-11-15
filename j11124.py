import json

with open('Personas.json', 'r') as openfile:
    json_object = json.load(openfile)           
print(json_object)
class Person:
    def __init__(self, firstname, lastname, birthday, age, gender, email):
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.age = age
        self.gender = gender
        self.email = email
    def print_info(self):
        print(self.firstname,self.lastname)
    def find_perason(self):
        print()

class main():
    while True:
            print("\n1. Pievienot cilveku")
            print("2. Paradit visus cilvekus")
            print("3. Meklet cilveku")
            print("4. Iziet")

            choice = input("Izveleties darbibu: ")

            if choice == '1':
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
                with open('Personas.json', 'r') as openfile:
                    json_object = json.load(openfile)           
                print(json_object)
                dictator = dictionary
                dictator.update(json_object)
                json_object = json.dumps(dictionary, indent=4)
                with open("Personas.json", "w", encoding="utf-8") as outfile:
                    outfile.write(json_object)
                print("Dati ierakstiti faila Personas.json.")


            elif choice == '2':
                pass

            elif choice == '3':
                print()
            elif choice == '4':
                print("Iziet no programas.")
                break

            else:
                print("Nepareiza izvēle, mēģiniet vēlreiz")


main()
'''
def add(args):
    with open(DATA_FILENAME, mode='r', encoding='utf-8') as feedsjson:
        feeds = json.load(feedsjson)
    with open(DATA_FILENAME, mode='w', encoding='utf-8') as feedsjson:
        entry = {}
        entry['name'] = args.name
        entry['url'] = args.url
        json.dump(entry, feedsjson)'''