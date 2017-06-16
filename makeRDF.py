import matplotlib.pyplot as plt
import copy

'''
Cl^- + CH3Cl
Cl1がイオン化
Cl2がCH3Clの一部
'''

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


    def plot(self,solute="methan",solvent="O",line_style = "-",color=None):
        if solute == "methan":
            plt.xlim(0,15)
            # plt.title(solute)
            if solvent=="O":
                plt.plot(self.r_array, self.meth_O_array,label=solute + "-" + solvent, linestyle=line_style,color = color)
            elif solvent=="H":
                plt.plot(self.r_array, self.meth_H1_array, label=solute + "-" + solvent, linestyle=line_style,color = color)
            else:
                print("please input \"O\" or \"H\"")
            plt.legend()
            # plt.show()
        elif solute == "Cl1":
            plt.xlim(0, 15)
            # plt.title(solute)
            if solvent == "O":
                plt.plot(self.r_array, self.Cl1_O_array, label=solute + "-" + solvent, linestyle=line_style,color = color)
            elif solvent == "H":
                plt.plot(self.r_array, self.Cl1_H1_array, label=solute + "-" + solvent, linestyle=line_style,color = color)
            else:
                print("please input \"O\" or \"H\"")
            plt.legend()
            # plt.show()
        elif solute == "Cl2":
            plt.xlim(0, 15)
            # plt.title(solute)
            if solvent == "O":
                plt.plot(self.r_array, self.Cl2_O_array, label=solute + "-" + solvent, linestyle=line_style,color = color)
            elif solvent == "H":
                plt.plot(self.r_array, self.Cl2_H1_array, label=solute + "-" + solvent, linestyle=line_style,color = color)
            else:
                print("please input \"O\" or \"H\"")
            plt.legend()
            # plt.show()
        else:
            print("please input \"metan\" or \"Cl1\" or \"Cl2\"")
        return plt

if __name__ == "__main__":
    # saddle = makeRDF("gr_saddle.mat")
    # saddle.input_file()
    # saddle.plot(solute="methan", solvent="O", color="orange", line_style="-")
    # saddle.plot(solute="methan", solvent="H", color="orange", line_style="--")
    # saddle.plot(solute="Cl1", solvent="O", color="blue", line_style="-")
    # saddle.plot(solute="Cl1", solvent="H", color="blue", line_style="--")
    # saddle.plot(solute="Cl2", solvent="O", color="green", line_style="-")
    # saddle.plot(solute="Cl2", solvent="H", color="green", line_style="--")

    stable = makeRDF("gr_edge.mat")
    stable.input_file()
    stable.plot(solute="methan", solvent="O", color="orange", line_style="-")
    stable.plot(solute="methan", solvent="H", color="orange", line_style="--")
    stable.plot(solute="Cl1", solvent="O", color="blue", line_style="-")
    stable.plot(solute="Cl1", solvent="H", color="blue", line_style="--")
    stable.plot(solute="Cl2", solvent="O", color="green", line_style="-")
    stable.plot(solute="Cl2", solvent="H", color="green", line_style="--")

    plt.savefig("all_edge_RDF.eps")
    plt.show()