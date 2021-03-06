import matplotlib.pyplot as plt

class interpData:
    alphaArray = [] #alpha[0,1]
    aArray = []     #position of Cl
    bArray = []     #position of CH3
    cArray = []     #position of Cl'
    abArray = []    #length a-b
    bcArray = []    #length b-c
    valueArray = [] #value of potential or free energy
    RCArray = []    #reaction coordinate
    def __init__(self,fileName,fileNameOfValue):
        self.alphaArray = []
        self.aArray = []
        self.bArray = []
        self.cArray = []
        self.abArray = []
        self.bcArray = []
        self.valueArray = []
        self.RCArray = []
        self.fileName = fileName
        self.fileNameOfValue = fileNameOfValue
        # print(self.aArray)
        # input()
        # print("My name is" + str(self.fileName))
        f = open(self.fileName, "r")
        while True:
            readLine = f.readline()
            if readLine == "":
                break
            else:
                alpha ,a,b,c = map(float,readLine.split())
                self.alphaArray.append(alpha)
                self.aArray.append(a)
                self.bArray.append(b)
                self.cArray.append(c)
        f.close()
        # print("ちゃんとデータ読めてるか確認" + str(len(self.aArray)))
        for i in range(len(self.aArray)):
            self.abArray.append(self.bArray[i] - self.aArray[i])
            self.bcArray.append(self.cArray[i] - self.bArray[i])

    def plotStringAlongAlpha(self,colorName):
        plt.plot(self.abArray,self.bcArray,linewidth = 1,color = colorName)
        #plt.show()

    def readValue(self):
        f = open(self.fileNameOfValue,"r")
        while True:
            readLine = f.readline()
            if readLine == "":
                break
            else:
                alpha, value = map(float,readLine.split())
                self.valueArray.append(value)
        # print(str(self.fileNameOfValue) + "  " + str(len(self.valueArray)))

    def plotValueAlongRC(self,colorName, line_style="-",label=None):
        for i in range(len(self.abArray)):
            self.RCArray.append(self.abArray[i] - self.bcArray[i])
        plt.plot(self.RCArray,self.valueArray, linewidth = 1, color = colorName, linestyle=line_style,label=label)
        plt.legend()

class AirData(interpData):
    def get_potential(self):
        import potentialOfSN2
        for i in range(len(self.abArray)):
            self.valueArray.append(potentialOfSN2.getPotential(self.abArray[i], self.bcArray[i]))

class OnlySolventFreeEnergy(AirData):
    def readValue(self):
        self.get_potential()
        f = open(self.fileNameOfValue, "r")
        i = 0
        while True:
            readLine = f.readline()
            if readLine == "":
                break
            else:
                alpha, value = map(float, readLine.split())
                self.valueArray[i] = value - self.valueArray[i]
                i += 1




if __name__ == "__main__":
    # air = interpData("interpAir.dat","alongStringAir.dat")
    air = AirData("interpNewData.dat", "alongStringWater.dat")
    air.get_potential()
    air.plotValueAlongRC("red",label="Gas-phase potential")

    water = interpData("interpNewData.dat","alongStringWater.dat")
    water.readValue()
    water.plotValueAlongRC("green",label="total free energy")

    sfe = OnlySolventFreeEnergy("interpNewData.dat", "alongStringWater.dat")
    sfe.readValue()
    sfe.plotValueAlongRC("blue", label="solvent contribution")
    # sfe.plotValueAlongRC("blue")
    # air.readValue()
    # air.plotValueAlongRC("red")
    # plt.savefig("valueAlongRC.png")
    plt.savefig("eachValue.png")
    plt.show()
    #
    # water.plotStringAlongAlpha("green")
    # air.plotStringAlongAlpha("red")
    # plt.show()

    # print(len(air.aArray))
    # print(len(water.aArray))

    # plt.savefig("strings.png")
