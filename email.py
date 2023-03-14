import pickle
import os

def menu(file):
    print("options menu:")
    print("press 1 for email address lookup")
    print("press 2 to add a contact")
    print("press 3 to change an email address" )
    print("press 4 to delete a contact" )
    print("press 'q' to save to file and close")
    option = input()
    match option:
        case "1":
            lookup()
            menu(file)
        case "2":
            update()
            menu(file)
        case "3": 
            update()
            menu(file)
        case "4":
            delete()
            menu(file)
        case "q":
            save(file)
            exit()
        #case _:
            #menu()
            
def lookup():
    print(thisdict.keys())
    if len(thisdict) <= 0:
        print("addressbook is empty")
    else: 
        name = input("type the name of the person whose email you would like:")
        if thisdict[name]:
            print(thisdict[name])
    
def update():
    name = input("type the name of the person:")
    email = input("type in their email: ")
    thisdict[name] = email
    
def delete():
    name = input("type the name of the person you would like to remove:")
    thisdict.pop(name)

def save(file):
    pickle.dump(thisdict, file)
    file.close()










if os.path.exists("addressbook.txt"):
    file = open("addressbook.txt", "rb+")
    thisdict = pickle.load(file)
    menu(file)
else:
    file = open("addressbook.txt", "ab+")
    thisdict = {}
    menu(file)