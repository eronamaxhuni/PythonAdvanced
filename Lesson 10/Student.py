class Student:
    def __init__(self,name,age):
        self.__name = name
        self.__age=age
    def get_name(self):
        return self.__name
    def get_name(self,name):
        self.__name=name
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age=age

donjeta=Student("donjeta",17)
print(donjeta.get_age())
donjeta.set_age(18)
print(donjeta.get_age())
