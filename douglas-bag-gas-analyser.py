from tabulate import tabulate

# Class for participants basic information
class DescriptiveData:
    def __init__(self, age, gender, height, mass, baromPress, roomTemp):
        self.__age = age
        self.__gender = gender
        self.__height = height
        self.__mass = mass
        self.__baromPress = baromPress
        self.__roomTemp = roomTemp

    def createDescriptiveTable(self):
        table = [["Age (yrs)", "Gender (M/F)", "Height (m)", "Mass (kg)", "Barometric Pressure (mmHg)", "Room Temperature (C)"],
                 [self.__age, self.__gender, self.__height, self.__mass, self.__baromPress, self.__roomTemp]]
        print("\nDescriptive data:")
        print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))