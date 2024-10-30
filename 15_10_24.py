class Person:
    def __init__(self, firstname, lastname, birthday, age, gender, email):
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.age = age
        self.gender = gender
        self.email = email
    def print_info(self):
        print(f"Person: {self.firstname,self.lastname}")
    def find_perason(self):
        print()

persona = Person("Nikita","Curkov","1488","78","True","curka@gmail.com")
persona.print_info()
persona.find_perason()


class main(Person):
    def __init__(self, firstname, lastname, birthday, age, gender, email):
        super().__init__(firstname, lastname, birthday, age, gender, email)
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

        elif choice == '2':
            print()

        elif choice == '3':
            firstname = input("Ievadiet vardu meklesanai: ")
            lastname = input("Ievadiet uzvardu meklesanai: ")

        elif choice == '4':
            print("Iziet no programas.")
            break

        else:
            print("Nepareiza izvēle, mēģiniet vēlreiz")

if __name__ == "__main__":
    main()