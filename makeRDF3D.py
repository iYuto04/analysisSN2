import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import subprocess
import makeInputFile
import os
from matplotlib import cm

class MakeRDFFiles:
    '''
    ストリングに沿った位置のファイルをinitializeで読み込ませてそれに対応する動径分布関数の値を取得する
    '''
    def __init__(self, file_name):
        self.alpha_array = []
        self.cordinate_array = []
        f = open(file_name, "r")
        for i in range(100): #max iteration 100
            readLine = f.readline()
            if readLine == "":
                break
            else:
                alpha, x1, x2, x3 = list(map(float, readLine.split()))
                self.alpha_array.append(alpha)
                self.cordinate_array.append([x1, x2, x3])
        f.close()

    def run_rism(self, r1=4.0, r2=1.8, alpha=1.0):
        makeInputFile.makeInputFile(r1, r2)
        subprocess.call(["zsh", "start_program.sh"])
        subprocess.call(["cp", "gr.mat", "./gr_files/gr{:03d}.mat".format(int(alpha*100))])

    def run_along_string(self):
        for i in range(len(self.alpha_array)):
            r1 = self.cordinate_array[i][1] - self.cordinate_array[i][0]
            r2 = self.cordinate_array[i][2] - self.cordinate_array[i][1]
            self.run_rism(r1=r1, r2=r2, alpha=self.alpha_array[i])



class RDF3D:
    '''
    ストリングに沿った動径分布関数を3Dプロットするクラス
    '''
    def __init__(self):
        try:
            os.chdir("gr_files")
        except:
            print("gr_filesディレクトリが見つかりません!")

        self.x = []
        self.y = []
        self.z = []

    def readRDF(self, file_name):
        f = open(file_name, "r")
        x = []
        z = []


        for i in range(380):
            readLine = f.readline()
            if readLine == "":
                break
            else:
                r, meth_O, meth_H1, meth_H2, Cl1_O, Cl1_H1, Cl1_H2, Cl2_O, Cl2_H1, Cl2_H2\
                 = map(float, readLine.split())
                x.append(r)
                z.append(Cl1_H1)

        if file_name == "gr100.mat":
            self.x = x
        self.z.append(z)

    def runAlongAlpha(self):
        number_of_files = 50 #gr.matのファイルの数
        initial_parameter = 0.02 #ストリングのパラメータの初期値が0.02からなので
        d_alpha = 0.02
        for i in range(number_of_files):
            alpha = d_alpha*i + initial_parameter
            self.y.append(alpha)
            self.readRDF("gr{:03d}.mat".format(int(round(alpha*100,0))))

    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111,projection='3d')
        ax = Axes3D(fig)
        X,Y = np.meshgrid(self.x, self.y)
        ax.plot_surface(X, Y, self.z, cmap=cm.coolwarm)
        plt.xlim(0, 12)
        plt.show()



def func(x,y):
    return x**2 + y**2

if __name__ == "__main__":
    # x = np.arange(-5, 5, 0.25)
    # y = np.arange(-5, 5, 0.25)
    # x = [1,2,3]
    # y = [10, 20]
    # X, Y = np.meshgrid(x, y)
    # Z = func(X, Y)
    # fig = plt.figure()
    # ax = Axes3D(fig)
    # ax.plot_wireframe(X, Y, Z)
    # plt.show()
    # print("the shape of X is", np.shape(X))
    # print("the shape of Y is ",np.shape(Y))
    # print("the shape of Z is ", np.shape(Z))
    # print(X)
    # print('-----')
    # print(Y)

    # rdf3d = MakeRDFFiles("interpNewData.dat")
    # rdf3d.run_along_string()

    rdf3d = RDF3D()
    rdf3d.runAlongAlpha()
    rdf3d.plot()
