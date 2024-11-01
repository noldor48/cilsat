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
                file = open("Personas.txt", "a", encoding="utf-8")
                lst = [] 
                firstname = input("Ievadiet vardu: ")
                lastname = input("Ievadiet uzvardu: ")
                birthday = input("Ievadiet birthday: ")
                age = input("Ievadiet vecumu: ")
                gender = input("Ievadiet dzimumu: ")
                email = input("Ievadiet email: ")
                lst.append(firstname + " " + lastname + " " + birthday + " " + age + " " + gender + " " + email + '\n')
                file.writelines(lst) 
                file.close() 
                print("Dati ierakstiti faila Personas.txt.") 
            elif choice == '2':
                file2 = open("Personas.txt", "r", encoding="utf-8")
                print(file2.read())
            elif choice == '3':
                print()
            elif choice == '4':
                print("Iziet no programas.")
                break

            else:
                print("Nepareiza izvēle, mēģiniet vēlreiz")

#persona = Person("Nikita","Curkov","1488","78","True","curka@gmail.com")
#persona.print_info()
#persona.find_perason()

main()