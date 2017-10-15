class Car():
    def __init__(self, make,year, model, color):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__color = color

    def set_make(self, make):
        self.__make = make

    def get_make(self):
        return self.__make

    def set_model(self, model):
        self.__model = model

    def get_model(self):
        return self.__model

    def set_year(self, year):
        self.__year = year

    def get_year(self):
        return self.__year

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def get_mileage(self):
        return self.__mileage

    def set_color(self, color):
        self.__color = color
    def get_color(self):
        return self.__color



class CompactCar(Car):
    def __init__(self, make = 'Toyota', model = 'Inova', year= '1965', color = 'black', hp = 325):
        super().__init__(make, model, year, color)
        self.__hp = hp

    def set_hp(self, hp):
        self.__hp = hp

    def get_hp(self):
        return self.__hp
a = CompactCar("Toyota", "Inova", "1965","black", 325 )#Determines the info of a dog on the first line
print(a.__dict__)

def loadwords(filename):
    with open(filename, 'r') as f:
         lines = [line for line in f if line.strip()]
    return lines
#Note that it has problems opening the txt file even when it is in the project
filename = input('Enter the filename: ')
file_lines = loadwords(filename)

