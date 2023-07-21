from tkinter import Toplevel

import uygulama
from izgara import *

from robot import robot
import requests

class lab:
    def problem2maze(self, matrix, R, C, kaynak):
        matrix = allblock(matrix, R, C)
        matrix = squareblock(matrix, R, C)
        x2 = 0
        y2 = 0
        createstartfinish(matrix, R, C)
        rows, cols = (R, C)
        counter = 0
        labellist = {}
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j].value == 1 and matrix[i][j].definitly == 1:
                    entry = Label(self, width=3, background='black')
                    labellist[counter] = entry
                elif matrix[i][j].value == 1 and matrix[i][j].definitly == 0:
                    entry = Label(self, width=3, background='black')
                    labellist[counter] = entry
                else:
                    entry = Label(self, width=3, background='white')
                    labellist[counter] = entry
                counter += 1
                entry.place(x=0 + x2, y=0 + y2)
                x2 += 28
            y2 += 22
            x2 = 0

        uyg = uygulama.uygulama(0,self)

        def startbutton():
            robot.robotstart(matrix, R, C, labellist,uyg)

        def onebyone():
            uygulama.uygulama.surestart(uyg)
            robot.robotstartstep(rbots, 1, 0, matrix, R, C, labellist, buton_1, buton_2,uyg)

        buton_1 = kaynak.Button(self, text='Başla', bg='white', fg='gray', font='verdana 17 bold', command=startbutton)
        buton_1.place(x=0, y=y2 + 40)
        rbots = robot(matrix, labellist, list)

        buton_2 = kaynak.Button(self, text='Adımla', bg='white', fg='gray', font='verdana 17 bold',
                                command=onebyone)  # robotu adım adım çalıştır
        buton_2.place(x=100, y=y2 + 40)
        return y2

    def problem1maze(self, kaynak,target_url,controller=0):
        #h = open('./txt/url1.txt', 'r')
        #h = open('http://bilgisayar.kocaeli.edu.tr/prolab2/url1.txt', 'r')


        def mazechange1():
            target_url = "http://bilgisayar.kocaeli.edu.tr/prolab2/url1.txt"
            buton_5.config(command=mazechange2,text="maze1")
            self.withdraw()
            newWindow = Toplevel(self)
            newWindow.title("Matrix")
            newWindow.geometry("600x600+120+120")
            newWindow.configure(bg='#F5ECC1')
            lab.problem1maze(newWindow,kaynak, target_url,controller=1)

        def mazechange2():
            target_url = "http://bilgisayar.kocaeli.edu.tr/prolab2/url2.txt"
            buton_5.config(command=mazechange1, text="maze2")
            self.withdraw()
            newWindow = Toplevel(self)
            newWindow.title("Matrix")
            newWindow.geometry("600x600+120+120")
            newWindow.configure(bg='#F5ECC1')
            lab.problem1maze(newWindow,kaynak,target_url,controller=0)

        response = requests.get(target_url)
        data = response.text
        i=0
        a=[]
        b=[]
        while i < len(data):
            if data[i]=='\n':
                b.append(a)
                a=[]
                i+=1
            else:
                a.append(int(data[i]))
                i+=1

        ''' content = h.readlines()
        b = []
        for line in content:
            a = []
            for i in line:
                if i.isdigit() == True:
                    a.append(int(i))
            b.append(a)'''
        R = len(b[0]) - 1
        C = len(b) - 1
        matrix = allblockformaze1(b, R, C)
        list=[]
        uyg=uygulama.uygulama(0,self)
        def startbutton():
            global z
            z=robot.startformaze1(rbots,R,C)
            buton_1.config(command=continuebutton)
            buton_2.config(command=continuebutton)
        def continuebutton():
            uygulama.uygulama.surestart(uyg)
            robot.robotroadfoundformaze1(rbots,z[0],z[1],z[2],z[3],R,C,buton_1,buton_2,uyg,list)
            #robot.robotroadfoundformaze1(rbots, 4, 0, 5, 4, R, C, buton_1)
        def closerroad():

            buton_4.config(command=findredroad())
        def findredroad():
            robot.robotroadfoundformaze1closer(rbots2,z[0],z[1],z[2],z[3],R,C)


        def yazdir():
            for i in range(R):
                for j in range(C):
                    if rbots.matrix[i][j].blocksize == 0 and rbots.matrix[i][j].definitly == 0:
                        #entry = Label(self, width=3, background='white')
                        rbots.labellist[(i * C) + j].config(background='white')
                    elif rbots.matrix[i][j].blocksize == 1 and rbots.matrix[i][j].definitly == 0:
                        #entry = Label(self, width=3, background='black')
                        rbots.labellist[(i * C) + j].config(background='black')
                    elif rbots.matrix[i][j].blocksize == 2 and rbots.matrix[i][j].definitly == 0:
                        #entry = Label(self, width=3, background='black')
                        rbots.labellist[(i * C) + j].config(background='black')
                    elif rbots.matrix[i][j].blocksize == 3 and rbots.matrix[i][j].definitly == 0:
                        #entry = Label(self, width=3, background='black')
                        rbots.labellist[(i * C) + j].config(background='black')
                    else:
                        #entry = Label(self, width=3, background='white')
                        rbots.labellist[(i * C) + j].config(background='white')
                    if rbots.matrix[i][j].visited == 1:
                        rbots.labellist[(i * C) + j].config(background='aqua')
                    #print(rbots.matrix[i][j].visited,end=' ')
                #print()

        labellist = createroadformaze1(self, matrix, R, C)
        rbots = robot(matrix=matrix, labellist=labellist[0])
        rbots2 = robot(matrix=matrix, labellist=labellist[0])

        buton_1 = kaynak.Button(self, text='Başla', bg='white', fg='gray', font='verdana 17 bold', command=startbutton)
        buton_1.place(x=0, y=labellist[1] + 40)
        buton_2 = kaynak.Button(self, text='adımla', bg='white', fg='gray', font='verdana 17 bold', command=startbutton)
        buton_2.place(x=100, y=labellist[1] + 40)
        buton_3 = kaynak.Button(self, text='yazdır', bg='white', fg='gray', font='verdana 17 bold', command=yazdir)
        buton_3.place(x=200, y=labellist[1] + 40)
        buton_4 = kaynak.Button(self, text='yakın yolu yazdır', bg='white', fg='gray', font='verdana 17 bold', command=closerroad)
        buton_4.place(x=300, y=labellist[1] + 40)
        buton_5 = kaynak.Button(self, bg='white', fg='gray', font='verdana 17 bold')
        buton_5.place(x=0, y=labellist[1] + 100)

        if controller == 0:
            print("hhh")
            buton_5.config(command=mazechange1,text='maze1')
        else:
            print("safasf")
            buton_5.config(command=mazechange2,text='maze2')



'''
def robotstart(matrix, r, c, labellist):
    start_x = 1
    start_y = 0
    list = []
    if matrix[start_x][start_y].changeable == 1:
        print('sa')
        labellist[((start_x) * 20) + start_y].config(background='aqua')
        matrix[start_x][start_y].blockcount += 1
    for i in range(r):
        for j in range(c):
            if matrix[i][j].changeable == 1:
                a = [matrix[i][j], i, j]
                list.append(a)
    rbots = robot(matrix, labellist, list)
    x = robot.robotroadfound(rbots, r=r, c=c, start_x=start_x, start_y=start_y)
    i = 0
    j = 0
    while i < r:
        while j < c:
            labellist[((i) * c) + j].config(text=str(x[i][j].blockcount))
            j += 1
        i += 1
        j = 0




def robotstartstep(rbots, start_x, start_y, matrix, r, c, labellist, buton1,buton2):
    list = []
    if matrix[start_x][start_y].changeable == 1:
        labellist[((start_x) * 20) + start_y].config(background='aqua')
        matrix[start_x][start_y].blockcount += 1
    for i in range(r):
        for j in range(c):
            if matrix[i][j].changeable == 1:
                a = [matrix[i][j], i, j]
                list.append(a)
    returninglist = []
    print('sa')
    global z
    z = robot.xxx(rbots, r=r, c=c, start_x=start_x, start_y=start_y, list=returninglist,matrix=matrix)
    def func():
        global z
        z=robotsteps2(z, r, c, rbots)
    buton2.config(command=func)

    def robotstartwherestopus():
        while True:
            controller = buton2.config(command=func())
            if controller==1:
                break
    buton1.config(command=robotstartwherestopus)

    def robotsteps(x, r, c, rbots):
        x = robot.xxx(rbots, r=r, c=c, start_x=x[2], start_y=x[3], list=x[1], matrix=x[0])
        return x

    def robotsteps2(x, r, c, rbots):
        x = robot.xxx(rbots, r=r, c=c, start_x=x[2], start_y=x[3], list=x[1], matrix=x[0])
        return x
    '''

'''
def robotstart(self, matrix, r, c):
    def gecici():
        robotfindroat(self,matrix, matrix2, r, c, labellist, buton_2)

    buton_2 = kaynak.Button(self, text='Başla', bg='white', fg='gray', font='verdana 17 bold', command=gecici)
    buton_3 = kaynak.Button(self, text='hızlı bitir', bg='white', fg='gray', font='verdana 17 bold')
    buton_2.place(x=0, y=540)
    buton_3.place(x=100, y=540)
    matrix2 = []
    matrix2 = allblockrobot(matrix2, r, c)
    matrix2 = squareblock(matrix2, r)
    x2 = 0
    y2 = 0
    counter = 0

    labellist = {}
    for i in range(r):
        a = []
        for j in range(c):
            if matrix2[i][j].value == 1 and matrix2[i][j].definitly == 1:
                entry = Label(self, width=3, background='gray')
                labellist[counter] = entry
            elif matrix2[i][j].blur == 1:
                entry = Label(self, width=3, background='aqua')
                labellist[counter] = entry
            else:
                entry = Label(self, width=3, background='white')
                labellist[counter] = entry
            
            counter += 1
            entry.place(x=0 + x2, y=0 + y2)
            x2 += 28
        y2 += 22
        x2 = 0
        createstartfinishrobot(matrix2, r)

def moverobot(self,matrix, matrix2, r, c, entry, start_x, start_y, finish_x, finish_y):
    real_time_x = start_x
    real_time_y = start_y
    if real_time_x != 0 and real_time_y != 0:
        matrix2[real_time_x][real_time_y - 1].blur = 0
        matrix2[real_time_x + 1][real_time_y].blur = 0
        matrix2[real_time_x - 1][real_time_y].blur = 0
        matrix2[real_time_x][real_time_y + 1].blur = 0
    elif real_time_x == 0:
        matrix2[real_time_x][real_time_y - 1].blur = 0
        matrix2[real_time_x + 1][real_time_y].blur = 0
        matrix2[real_time_x][real_time_y + 1].blur = 0
    elif real_time_y == 0:
        matrix2[real_time_x + 1][real_time_y].blur = 0
        matrix2[real_time_x - 1][real_time_y].blur = 0
        matrix2[real_time_x][real_time_y + 1].blur = 0
        if matrix[real_time_x + 1][real_time_y].changeable == 1:
            print('sa')
            entry[((real_time_x + 1)*20) + real_time_y].config(background='white')
        else:
            print('as')
            entry[((real_time_x + 1)*20) + real_time_y].config(background='gray')
        if matrix[real_time_x - 1][real_time_y].changeable == 1 and matrix[real_time_x - 1][real_time_y].definitly == 0:
            print('sasss')
            entry[((real_time_x - 1)*20) + real_time_y].config(background='white')
        else:
            print('saaaaaaaaaa')
            entry[((real_time_x - 1)*20) + real_time_y].config(background='gray')
        if matrix[real_time_x][real_time_y + 1].changeable == 1 and matrix[real_time_x][real_time_y + 1].definitly == 0:
            entry[(real_time_x*20) + (real_time_y + 1)].config(background='white')
            print('dskjhfgksdjg')
        else:
            print('46546545616')
            entry[(real_time_x*20) + (real_time_y + 1)].config(background='gray')
    else:
        print('boş')
    #beyazlatma tamam ilerletme kaldı

def robotfindroat(self,matrix, matrix2, r, c, entry, button):
    def move():
        moverobot(self,matrix, matrix2, r, c, entry, start_x, start_y, finish_x, finish_y)

    start_x = 1
    start_y = 0
    finish_x = 18
    finish_y = 19

    button.config(command=move)
    a = 20

    if matrix[start_x][start_y].value == 0:
        entry[start_x * a + start_y].config(background='white')
        entry[finish_x * a + finish_y].config(background='white')
'''

'''
def createstartfinish(self, matrix, R):
    start_x = 1
    start_y = 0
    finish_x = R - 2
    finish_y = R - 1
    matrix[start_x][start_y] = block(1, 0, 0)
    matrix[finish_x][finish_y] = block(1, -1, 0)
    matrix[-2][-2] = block(0, 0, 0)
    fakeroad(self,matrix, R)

def fakeroad(self, matrix, R):
    # b = ['sol', 'alt', 'sag', 'ust']
    row = 0
    column = 0
    i = 0
    a = int
    check = 0
    list = []
    while matrix[row][column].changeable != -1:
        b = random.randint(0, 3)
        if row == 0 and column == 0 and matrix[row][column - 1].changeable == 0:
            print('girdii')
            a = random.randint(0, 1)
            a = 1
            if a == 1:
                row += 1
            elif a == 0:
                column += 1

        else:
            if a == 1:

                if column == 19:
                    column-=1
                if row == 19:
                    row-=1
                if matrix[row][column + 1].changeable == -1:
                    print('1')
                    column += 1
                    matrix[row][column].changeable = 1
                    matrix[row][column + 1].value = 0
                elif matrix[row ][column].changeable == -1:
                    print('2')
                    row += 1
                    matrix[row + 1][column].changeable == 1
                    matrix[row + 1][column].value = 0
                elif matrix[row + 1][column + 1].changeable == -1:
                    gecici = random.randint(0,1)
                    if gecici == 0:
                        matrix[row][column + 1].changeable == 1
                        matrix[row][column + 1].value = 0
                    else:
                        matrix[row + 1][column].changeable == 1
                        matrix[row + 1][column].value = 0


                else:

                    if b == 0 and matrix[row][column - 1].definitly == 0 and matrix[row][column - 1].changeable == 0 and \
                            (matrix[row + 1][column - 1].changeable == 0 and matrix[row - 1][
                                column - 1].changeable == 0) and \
                            matrix[row][column - 2].changeable == 0:
                        print('bir')
                        column -= 1
                    elif b == 1 and matrix[row + 1][column].definitly == 0 and matrix[row + 1][
                        column].changeable == 0 and \
                            (matrix[row + 1][column - 1].changeable == 0 and matrix[row + 1][
                                column + 1].changeable == 0) and \
                            matrix[row + 2][column].changeable == 0:
                        row += 1
                        print('iki')
                    elif b == 2 and matrix[row][column + 1].definitly == 0 and matrix[row][
                        column + 1].changeable == 0 and \
                            (matrix[row - 1][column + 1].changeable == 0 and matrix[row + 1][
                                column + 1].changeable == 0) and \
                            matrix[row][column + 2].changeable == 0:
                        print('üç')
                        column += 1
                    elif b == 3 and matrix[row - 1][column].definitly == 0 and matrix[row - 1][
                        column].changeable == 0 and \
                            (matrix[row - 1][column + 1].changeable == 0 and matrix[row - 1][
                                column - 1].changeable == 0) and \
                            matrix[row - 2][column].changeable == 0:
                        row -= 1
                        print('dört')
                    else:

                        gecici = random.randint(0, len(list)-1)
                        if matrix[list[gecici][0]][list[gecici][1]].changeable == 1 and matrix[list[gecici][0]][list[gecici][1]].cantreturn == 0:
                            check = 0
                            row=list[gecici][0]
                            column = list[gecici][1]
                            # matrix[row][column] = block(matrix[row][column].definitly,matrix[row][column].changeable,matrix[row][column].value,1)
                            matrix[row][column].cantreturn = 1


                        else:  # şu siktiğimin geri dönüp rastgele yol bulmasını çözzzzzzzzzzzzzzzz
                            #print(list[gecici])
                            
                            if i == 100000:
                                break
                            else:
                                i += 1

        #print(row,column,matrix[row][column].changeable)
        #print(matrix[row][column].cantreturn)
        if check==0:
            matrix[row][column].changeable = 1 #= block(0, 1, 0)
            matrix[row][column].value = 0
            gecici=[row,column]
            if len(list)!=0:
                if gecici!=list[-1]:
                    list.append(gecici)
            else:
                list.append(gecici)
        if row==17 and column==18:
            row=random.randint(0,18)
        check=0
        #print(row, column, matrix[row][column].cantreturn)
'''
