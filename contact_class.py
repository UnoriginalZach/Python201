class Contact:
    def __init__(self, __name, __age, __address, __number):
        self.__name = __name
        self.__age = __age
        self.__address = __address
        self.__number = __number
    def set_name(self, name):
        self.__name = name;
    def get_name(self):
        return self.__name
    def set_number(self,number):
        self.__number = number
    def get_number(self):
        return self.__number
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age
    def get_address(self):
        return self.__address
    def set_age(self, address):
        self.__address = address
        

my_contact = Contact("Freddy", 39, "123 madeup ave. anyplace, OR", 8675309 )
friend1 = Contact("Zach", 28, "321 nowhere way, anyplace OR", 18008882500)
friend2 = Contact("Chris", 36, "213 rainbow rd, anyplace, OR", 18005552368)