from tabulate import tabulate

# Class for methods in order to ask for user input
class UserInput:
    def inputAge(self):
        while True:
            try:
                age = int(input("Please enter your age (yrs): "))
                break
            except ValueError:
                print("\nYour input was invalid. Please try again.")
                continue
        return age

    def inputGender(self):
        while True:
            gender = str(input("Please enter your gender (M/F): "))
            if gender == "M" or gender == "F":
                break
            else:
                print("\nYour input was invalid. Please try again.")
        return gender

    def inputHeight(self):
        while True:
            try:
                height = float(input("Please enter your height (m): "))
                break
            except ValueError:
                print("\nYour input was invalid. Please try again.")
                continue
        return height

    def inputMass(self):
        while True:
            try:
                mass = float(input("Please enter your mass (kg): "))
                break
            except ValueError:
                print("\nYour input was invalid. Please try again.")
                continue
        return mass

    def inputBaromPress(self):
        while True:
            try:
                baromPress = float(input("Please enter the barometric pressure (mmHg): "))
                break
            except ValueError:
                print("\nYour input was invalid. Please try again.")
                continue
        return baromPress

    def inputRoomTemp(self):
        while True:
            try:
                roomTemp = float(input("Please enter the room temperature (C): "))
                break
            except ValueError:
                print("\nYour input was invalid. Please try again.")
                continue
        return roomTemp

    def inputNumBags(self):
        while True:
            try:
                numBags = int(input("Please enter the number of Douglas Bags you would like to record: "))
                break
            except ValueError:
                print("\nYour input was invalid. Please try again.")
                continue
        return numBags

    def inputTime(self):
        while True:
            try:
                time = int(input("Please enter the time in seconds this Douglas Bag was sampled (s): "))
                break
            except ValueError:
                print("\nYour input was invalid. Please try again.")
                continue
        return time

    def inputAppliedMass(self):
        while True:
            try:
                appliedMass = float(input("Please enter the applied mass for this Douglas Bag sample (kg): "))
                break
            except ValueError:
                print("\nYour input was invalid. Please try again.")
                continue
        return appliedMass

    def inputHeartRate(self):
        while True:
            try:
                heartRate = float(input("Please enter the average HR for this Douglas Bag sample (bpm): "))
                break
            except ValueError:
                print("\nYour input was invalid. Please try again.")
                continue
        return heartRate

    def inputFlywheelCount(self):
        while True:
            try:
                flywheelCount = int(input("Please enter the flywheel count for this Douglas Bag sample: "))
                break
            except ValueError:
                print("\nYour input was invalid. Please try again.")
                continue
        return flywheelCount

    def inputFeO2(self):
        while True:
            try:
                feO2 = float(input("Please enter the FEO2 for this Douglas Bag sample (%): "))
                break
            except ValueError:
                print("\nYour input was invalid. Please try again.")
                continue
        return feO2

    def inputFeCO2(self):
        while True:
            try:
                feCO2 = float(input("Please enter the FECO2 for this Douglas Bag sample (%): "))
                break
            except ValueError:
                print("\nYour input was invalid. Please try again.")
                continue
        return feCO2

    def inputSampleVolume(self):
        while True:
            try:
                sampleVolume = float(input("Please enter the sample volume during gas analysis for this Douglas Bag sample (L): "))
                break
            except ValueError:
                print("\nYour input was invalid. Please try again.")
                continue
        return sampleVolume

    def inputRemainVolume(self):
        while True:
            try:
                remainVolume = float(input("Please enter the remaining volume in the Douglas Bag for this Douglas Bag sample (L): "))
                break
            except ValueError:
                print("\nYour input was invalid. Please try again.")
                continue
        return remainVolume

    def inputBagTemp(self):
        while True:
            try:
                bagTemp = float(input("Please enter the Douglas Bag temperature for this Douglas Bag sample (C): "))
                break
            except ValueError:
                print("\nYour input was invalid. Please try again.")
                continue
        return bagTemp

    # Calls other methods in this class to prompt the user to input Douglas Bag equipment data and append them to a 2D array
    def inputAllBagData(self, numBags):
        allBagData = []
        for i in range(numBags):
            print("\nDouglas Bag " + str(i + 1) + ":")
            dataPerBag = []
            dataPerBag.append(self.inputTime())
            dataPerBag.append(self.inputAppliedMass())
            dataPerBag.append(self.inputHeartRate())
            dataPerBag.append(self.inputFlywheelCount())
            dataPerBag.append(self.inputFeO2())
            dataPerBag.append(self.inputFeCO2())
            dataPerBag.append(self.inputSampleVolume())
            dataPerBag.append(self.inputRemainVolume())
            dataPerBag.append(self.inputBagTemp())
            allBagData.append(dataPerBag)
        return allBagData

# Class for descriptive data
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

# Class for gas analysis data
class GasAnalysisData:
    def __init__(self, numBags, baromPress, allBagData):
        self.__numBags = numBags
        self.__baromPress = baromPress
        self.__allBagData = allBagData # Change to self.__allBagData later

    def __calculatePowerOutput(self, bagNum):
        powerOutput = ((self.__allBagData[bagNum][1] * 9.81) * (1.622 * self.__allBagData[bagNum][3]) / self.__allBagData[bagNum][0])
        self.__allBagData[bagNum].append(round(powerOutput, 2))

    def __calculateTotalVolume(self, bagNum):
        totalVolume = (self.__allBagData[bagNum][6] + self.__allBagData[bagNum][7])
        self.__allBagData[bagNum].append(round(totalVolume, 2))

    def __calculateVeAtps(self, bagNum):
        veAtps = ((self.__allBagData[bagNum][10]) / (self.__allBagData[bagNum][0] / 60))
        self.__allBagData[bagNum].append(round(veAtps, 2))

    def __calculateVeStpd(self, bagNum):
        swvp = ((1.001 * self.__allBagData[bagNum][8]) - 4.19)
        veStpd = (self.__allBagData[bagNum][11] * ((self.__baromPress - swvp) / 760) * (273 / (273 + self.__allBagData[bagNum][8])))
        self.__allBagData[bagNum].append(round(veStpd, 2))

    def __calculateVo2(self, bagNum):
        fiN2 = 79.04
        feN2 = (100 - (self.__allBagData[bagNum][4] + self.__allBagData[bagNum][5]))
        vi = ((feN2 / fiN2) * self.__allBagData[bagNum][12])
        vo2Insp = (vi * (20.93 / 100))
        vo2Exp = (self.__allBagData[bagNum][12] * (self.__allBagData[bagNum][4] / 100))
        vo2 = (vo2Insp - vo2Exp)
        self.__allBagData[bagNum].append(round(vo2, 2))

    def __calculateVco2(self, bagNum):
        fiN2 = 79.04
        feN2 = (100 - (self.__allBagData[bagNum][4] + self.__allBagData[bagNum][5]))
        vi = ((feN2 / fiN2) * self.__allBagData[bagNum][12])
        vco2Insp = (vi * (0.03 / 100))
        vco2Exp = (self.__allBagData[bagNum][12] * (self.__allBagData[bagNum][5] / 100))
        vco2 = (vco2Exp - vco2Insp)
        self.__allBagData[bagNum].append(round(vco2, 2))

    def __calculateRer(self, bagNum):
        rer = (self.__allBagData[bagNum][14] / self.__allBagData[bagNum][13])
        self.__allBagData[bagNum].append(round(rer, 2))
        
    # Calls all 'calculate' methods in this class in a for loop for the number of bags there are
    def appendAllBagData(self):
        for i in range(self.__numBags):
            self.__calculatePowerOutput(i)
            self.__calculateTotalVolume(i)
            self.__calculateVeAtps(i)
            self.__calculateVeStpd(i)
            self.__calculateVo2(i)
            self.__calculateVco2(i)
            self.__calculateRer(i)

    # Creates the gas analysis data table
    def createGasAnalysisTable(self):
        table = [] # 2D array which will contain columnHeaders and each of the sub-arrays of columnCells
        columnHeaders = ["Data"]
        columnCells = [["Time (s)"], ["Applied Mass (kg)"], ["Heart Rate (bpm)"], ["Flywheel Count"], ["FEO2 (%)"], ["FECO2 (%)"],
                       ["Sample Volume (L)"], ["Remaining Volume (L)"], ["Bag Temperature (C)"], ["Power Output (W)"],
                       ["Total Bag Volume (L)"], ["VE ATPS (L/min)"], ["VE STPD (L/min)"], ["VO2 (L/min)"], ["VCO2 (L/min)"],
                       ["RER"]]

        # Appends the bag numbers to the columnHeaders array
        for i in range(self.__numBags):
            columnHeaders.append("Bag " + str(i + 1))

        # Appends the columnHeaders array into the table array
        table.append(columnHeaders)

        # Appends the value in allBagData to each of the respective columnCells sub-arrays
        for j in range(self.__numBags):
            columnCells[0].append(self.__allBagData[j][0])
            columnCells[1].append(self.__allBagData[j][1])
            columnCells[2].append(self.__allBagData[j][2])
            columnCells[3].append(self.__allBagData[j][3])
            columnCells[4].append(self.__allBagData[j][4])
            columnCells[5].append(self.__allBagData[j][5])
            columnCells[6].append(self.__allBagData[j][6])
            columnCells[7].append(self.__allBagData[j][7])
            columnCells[8].append(self.__allBagData[j][8])
            columnCells[9].append(self.__allBagData[j][9])
            columnCells[10].append(self.__allBagData[j][10])
            columnCells[11].append(self.__allBagData[j][11])
            columnCells[12].append(self.__allBagData[j][12])
            columnCells[13].append(self.__allBagData[j][13])
            columnCells[14].append(self.__allBagData[j][14])
            columnCells[15].append(self.__allBagData[j][15])

        # Appends the columnCells sub-arrays into the table array
        for k in range(16):
            table.append(columnCells[k])

        print("\nGas analysis data:")
        print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))

# Main program
# Creating new UserInput object
newUserInput = UserInput()

# Prompts the user to input all descriptive data
age = newUserInput.inputAge()
gender = newUserInput.inputGender()
height = newUserInput.inputHeight()
mass = newUserInput.inputMass()
baromPress = newUserInput.inputBaromPress()
roomTemp = newUserInput.inputRoomTemp()

# Creating new DescriptiveData object to assign their attributes
newDescriptiveData = DescriptiveData(age, gender, height, mass, baromPress, roomTemp)

# Prompts the user to input the number of Douglas Bags they want to record
numBags = newUserInput.inputNumBags()

# Prompts the user to input all data collected from Douglas Bag equipment needed for calculations
# Prompts loops based on the number of Douglas Bags are being recorded
allBagData = newUserInput.inputAllBagData(numBags)

# Createing new GasAnalysisData object to assign their attributes
newGasAnalysisData = GasAnalysisData(numBags, baromPress, allBagData)

# Calculates all the values and appends them to the already existing allBagData 2D array
newGasAnalysisData.appendAllBagData()

# Creating and displaying the tables
newDescriptiveData.createDescriptiveTable()
newGasAnalysisData.createGasAnalysisTable();
