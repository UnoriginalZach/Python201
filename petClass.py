class pet:
    def __init__(self, __name, __animal_type, __age):
        self.__name = __name
        self.__animal_type = __animal_type
        self.__age = __age
    def __str__(self):
        return f"my pet is a {self.__animal_type} named {self.__name} and they are {self.__age} years old)"
    def set_name(self, name):
        self.__name = name;
    def get_name(self):
        return self.__name
    def set_animal_type(self,animal_type):
        self.__animal_type = animal_type
    def get_animal_type(self):
        return self.__animal_type
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age
        
name = input("what is your pet's name:")
age = input("what is your pet's age:")
animal_type = input("what type of pet do you have:")

my_pet = pet(name, animal_type, age)

print(my_pet)