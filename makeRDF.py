import matplotlib.pyplot as plt

class makeRDF:
    def __init__(self, file_name):
        self.file_name = file_name

    def input_file(self):
        MAX_ITERATION = 1000
        self.r_array = []
        self.meth_O_array = []
        self.meth_H1_array =[]
        self.meth_H2_array = []
        self.Cl1_O_array = []
        self.Cl1_H1_array = []
        self.Cl1_H2_array = []
        self.Cl2_O_array = []
        self.Cl2_H1_array = []
        self.Cl2_H2_array = []
        f = open(self.file_name, "r")
        for i in range(MAX_ITERATION):
            if f.readline() == "":
                break
            r,meth_O, meth_H1, meth_H2, Cl1_O, Cl1_H1, Cl1_H2, Cl2_O, Cl2_H1, Cl2_H2\
            = map(float, f.readline().split())
            # print(f.readline())
            self.r_array.append(r)
            self.meth_O_array.append(meth_O)
            self.meth_H1_array.append(meth_H1)
            self.meth_H2_array.append(meth_H2)
            self.Cl1_O_array.append(Cl1_O)
            self.Cl1_H1_array.append(Cl1_H1)
            self.Cl1_H2_array.append(Cl1_H2)
            self.Cl2_O_array.append(Cl2_O)
            self.Cl2_H1_array.append(Cl2_H1)
            self.Cl2_H2_array.append(Cl2_H2)


    def plot(self,solute="methan",line_style = "-"):
        if solute == "methan":
            plt.xlim(0,15)
            plt.title(solute)
            plt.plot(self.r_array, self.meth_O_array,label="O", linestyle=line_style)
            plt.plot(self.r_array, self.meth_H1_array, label="H", linestyle=line_style)
            plt.legend()
            # plt.show()
        elif solute == "Cl1":
            plt.xlim(0, 15)
            plt.title(solute)
            plt.plot(self.r_array, self.Cl1_O_array, label="O", linestyle=line_style)
            plt.plot(self.r_array, self.Cl1_H1_array, label="H", linestyle=line_style)
            plt.legend()
            # plt.show()
        elif solute == "Cl2":
            plt.xlim(0, 15)
            plt.title(solute)
            plt.plot(self.r_array, self.Cl2_O_array, label="O", linestyle=line_style)
            plt.plot(self.r_array, self.Cl2_H1_array, label="H", linestyle=line_style)
            plt.legend()
            # plt.show()
        else:
            print("please input \"metan\" or \"Cl1\" or \"Cl2\"")
        return plt

if __name__ == "__main__":
    saddle = makeRDF("gr_saddle.mat")
    saddle.input_file()
    saddle.plot(solute="Cl1")

    # edge = makeRDF("gr_edge.mat")
    # edge.input_file()
    # edge.plot(solute="Cl2",line_style="-")

    plt.savefig("Cl1_saddle_RDF.png")
    plt.show()