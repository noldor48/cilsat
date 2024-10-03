class Person:
    def __init__(self, firstname, lastname, birthday, age, gender, email):
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.age = age
        self.gender = gender
        self.email = email

    def __str__(self):
        return f"Vards: {self.firstname},Uzvards: {self.lastname}, Vecums: {self.age},Dzimums: {self.gender}, Email: {self.email}"

class workpeople:
    def __init__(self):
        self.people = []
    def add_person(self, firstname, lastname, birthday, age, gender, email):
        person = Person(firstname, lastname, birthday, age, gender, email)
        self.people.append(person)
    def display_people(self):
        if not self.people:
            print("Nav pierakstito cilveku.")
            return
        for person in self.people:
            print(person)

    def find_person(self, firstname):
        for person in self.people:
            if person.firstname.lower() == firstname.lower():
                return person
        return None
    
class main:
        tracker =workpeople()
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
                tracker.add_person(firstname, lastname, birthday, age, gender, email)

            elif choice == '2':
                person = tracker.find_person(firstname)

                if person:
                    print(person)
                else:
                    print("Cilveks nav atrasts.")
            elif choice == '3':
                firstname = input("Ievadiet vardu meklesanai: ")
                lastname = input("Ievadiet uzvardu meklesanai: ")
                if person:
                    print(person)
                else:
                    print("Cilveks nav atrasts.")

            elif choice == '4':
                print("Iziet no programas.")
                break

            else:
                print("Nepareiza izvēle, mēģiniet vēlreiz")

if __name__ == "__main__":
    main()
#main()

