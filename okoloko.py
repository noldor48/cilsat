class Person:
    '''def __init__(self,firstname,lastname,email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email'''


    def add_person(self,firstname,lastname,email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        print("Jaunas personas izveidosana.")
        firstname = input("Ievadiet vardu: ")
        lastname = input("Ievadiet uzvardu: ")
        email = input("Ievadiet email: ")


    def view_people(self):
        return (self.firstname, self.lastname, self.email)

'''class main():
    while True:
        print("1. Pievienot cilveku")
        print("2. Paradit visus cilvekus")
        print("3. Meklet cilveku")
        print("4. Iziet")
        choise = input("Izveleties darbibu: ")

        people = []

        if choise == "1":
            print()
            add_person()

        elif choise == "2":
            print()
            view_people()
        elif choise == "3":
            print()
        elif choise == "4":
            break
        else:
            print("Nepareiza darbiba.")'''

a = Person()
a.add_person("German","Alik","idi nax")
a.view_people()