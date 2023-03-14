class Patient:
    def __init__(self, name, address, phone_number, e_contact):
        for x, y in name.items():
            self.name[x] = y
        for x, y in address.items():
            self.address[x] = y
        for x, y in e_contact.items():
            self.e_contact[x] = y
        self.phone_number = phone_number
        
name = dict()
address = dict()
e_contact = dict()

name['first'] = input("enter patient's first name: ")
name['middle'] = input("enter patient's middle name: ")
name['last'] = input("enter patient's last name: ")

x = Patient(name)