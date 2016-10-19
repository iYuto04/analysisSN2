import matplotlib.pyplot as plt

class interpData:
    alphaArray = []
    aArray = []
    bArray = []
    cArray = []
    def __init__(self,fileName):
        self.alphaArray = []
        self.aArray = []
        self.bArray = []
        self.cArray = []
        self.fileName = fileName
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
            self.cArray[i] -= self.bArray[i]
            self.bArray[i] -= self.aArray[i]

    def plotValueAlongAlpha(self,colorName):
        plt.plot(self.bArray,self.cArray,linewidth = 1,color = colorName)
        #plt.show()




water = interpData("interpNewData.dat")
water.plotValueAlongAlpha("green")
air = interpData("interpAir.dat")
air.plotValueAlongAlpha("red")

print(len(air.aArray))
print(len(water.aArray))

plt.show()