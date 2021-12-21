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

# Class for methods in order to ask for user input
class UserInput:
    def inputAge(self):
        while True:
            try:
                age = int(input("Please enter your age (yrs): "))
                break
            except ValueError:
                print("Your input was invalid. Please try again.")
                continue
        return age

    def inputGender(self):
        while True:
            gender = str(input("Please enter your gender (M/F): "))
            if gender == "M" or gender == "F":
                break
            else:
                print("Your input was invalid. Please try again.")
        return gender

    def inputHeight(self):
        while True:
            try:
                height = float(input("Please enter your height (m): "))
                break
            except ValueError:
                print("Your input was invalid. Please try again.")
                continue
        return height

    def inputMass(self):
        while True:
            try:
                mass = float(input("Please enter your mass (kg): "))
                break
            except ValueError:
                print("Your input was invalid. Please try again.")
                continue
        return mass

    def inputBaromPress(self):
        while True:
            try:
                baromPress = float(input("Please enter the barometric pressure (mmHg): "))
                break
            except ValueError:
                print("Your input was invalid. Please try again.")
                continue
        return baromPress

    def inputRoomTemp(self):
        while True:
            try:
                roomTemp = float(input("Please enter the room temperature (C): "))
                break
            except ValueError:
                print("Your input was invalid. Please try again.")
                continue
        return roomTemp

    def inputNumBags(self):
        while True:
            try:
                numBags = int(input("Please enter the number of Douglas Bags you would like to record: "))
                break
            except ValueError:
                print("Your input was invalid. Please try again.")
                continue
        return numBags

# Main program
newUserInput = UserInput()
age = newUserInput.inputAge()
gender = newUserInput.inputGender()
height = newUserInput.inputHeight()
mass = newUserInput.inputMass()
baromPress = newUserInput.inputBaromPress()
roomTemp = newUserInput.inputRoomTemp()

newDescriptiveData = DescriptiveData(age, gender, height, mass, baromPress, roomTemp)
#newDescriptiveData.createDescriptiveTable()
print("\n")

numBags = newUserInput.inputNumBags()