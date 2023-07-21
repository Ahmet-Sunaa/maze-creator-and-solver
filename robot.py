import random
from tkinter import Tk

from numpy.random.mtrand import randint
from tkinter import Label

import uygulama


class robot:
    def __init__(self, matrix, labellist, changeablelist=0):
        self.matrix = matrix
        self.labellist = labellist
        self.changeablelist = changeablelist

    def robotstart(matrix, r, c, labellist,uyg):
        start_x = 1
        start_y = 0
        list = []
        if matrix[start_x][start_y].changeable == 1:
            labellist[((start_x) * 20) + start_y].config(background='aqua')
            matrix[start_x][start_y].blockcount += 1
        for i in range(r):
            for j in range(c):
                if matrix[i][j].changeable == 1:
                    a = [matrix[i][j], i, j]
                    list.append(a)
        rbots = robot(matrix, labellist, list)
        uygulama.uygulama.surestart(uyg)
        x = robot.robotroadfound(rbots, r=r, c=c, start_x=start_x, start_y=start_y,uyg=uyg)
        i = 0
        j = 0
        while i < r:
            while j < c:
                labellist[((i) * c) + j].config(text=str(x[i][j].blockcount))
                j += 1
            i += 1
            j = 0

    def robotroadfound(self, r, c, start_x, start_y,uyg):
        list = []
        z=0
        while z<r*c:
            if self.matrix[start_x][start_y + 1].changeable == 1 and self.matrix[start_x][start_y + 1].visited == 0:
                self.matrix[start_x][start_y].visited == 1
                start_y = start_y + 1
            elif self.matrix[start_x + 1][start_y].changeable == 1 and self.matrix[start_x + 1][start_y].visited == 0:
                self.matrix[start_x][start_y].visited == 1
                start_x = start_x + 1
            elif self.matrix[start_x][start_y - 1].changeable == 1 and self.matrix[start_x][start_y - 1].visited == 0:
                self.matrix[start_x][start_y].visited == 1
                start_y = start_y - 1
            elif self.matrix[start_x - 1][start_y].changeable == 1 and self.matrix[start_x - 1][start_y].visited == 0:
                self.matrix[start_x][start_y].visited = 1
                start_x = start_x - 1
            else:
                i = 0
                while i < len(list):
                    a = list[i][0]
                    b = list[i][1]
                    if self.matrix[a][b].visited == 1 and ((self.matrix[a][b + 1].changeable == 1 and self.matrix[a][b + 1].visited == 0) or (self.matrix[a + 1][b].changeable == 1 and self.matrix[a + 1][b].visited == 0) or (self.matrix[a][b - 1].changeable == 1 and self.matrix[a][b - 1].visited == 0) or (self.matrix[a - 1][b].changeable == 1 and self.matrix[a - 1][b].visited == 0)):
                        start_x = a
                        start_y = b
                        self.labellist[((start_x) * c) + start_y].config(background='blue')
                    i += 1

            if self.matrix[start_x][start_y].changeable == 1:
                self.labellist[((start_x) * c) + start_y].config(background='aqua')
                self.matrix[start_x][start_y].blockcount += 1
                self.matrix[start_x][start_y].visited = 1
                list = self.samelistobjectdelete(list, start_x, start_y)
                if start_x == r - 2 and start_y == c - 2:
                    uygulama.uygulama.surefinish(uyg)
                    uygulama.uygulama.matrixwriter(uyg,self.matrix)
                    break
            z+=1
        if z == r*c:
            print('çıkış bulunamadı')
        return self.matrix

    def robotstartstep(rbots, start_x, start_y, matrix, r, c, labellist, buton1, buton2,uyg):
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
        global z
        z = robot.robotstepsroadfound(rbots, r=r, c=c, start_x=start_x, start_y=start_y, list=returninglist,
                                      matrix=matrix,uyg=uyg)

        def func():
            global z
            z = robotsteps(z, r, c, rbots,uyg)
            if len(z)==0:
                return 1
        buton2.config(command=func)

        def robotstartwherestop():
            a=0
            while a<r*c:
                controller = buton2.config(command=func())
                if controller == 1:
                    break
                a+=1

        buton1.config(command=robotstartwherestop)

    def robotstepsroadfound(self, matrix, r, c, start_x, start_y,uyg ,list):

        if matrix[start_x][start_y + 1].changeable == 1 and matrix[start_x][start_y + 1].visited == 0:
            self.matrix[start_x][start_y].visited == 1
            start_y = start_y + 1
        elif matrix[start_x + 1][start_y].changeable == 1 and matrix[start_x + 1][start_y].visited == 0:
            self.matrix[start_x][start_y].visited == 1
            start_x = start_x + 1
        elif matrix[start_x][start_y - 1].changeable == 1 and matrix[start_x][start_y - 1].visited == 0:
            matrix[start_x][start_y].visited == 1
            start_y = start_y - 1
        elif matrix[start_x - 1][start_y].changeable == 1 and matrix[start_x - 1][start_y].visited == 0:
            matrix[start_x][start_y].visited = 1
            start_x = start_x - 1
        else:
            i = 0
            while i < len(list):
                a = list[i][0]
                b = list[i][1]
                if matrix[a][b].visited == 1 and (
                        (matrix[a][b + 1].changeable == 1 and matrix[a][b + 1].visited == 0) or (
                        matrix[a + 1][b].changeable == 1 and matrix[a + 1][b].visited == 0) or (
                                matrix[a][b - 1].changeable == 1 and matrix[a][b - 1].visited == 0) or (
                                matrix[a - 1][b].changeable == 1 and matrix[a - 1][b].visited == 0)):
                    start_x = a
                    start_y = b
                    self.labellist[((start_x) * c) + start_y].config(background='blue')
                i += 1

        if matrix[start_x][start_y].changeable == 1:
            self.labellist[((start_x) * c) + start_y].config(background='aqua')
            matrix[start_x][start_y].blockcount += 1
            matrix[start_x][start_y].visited = 1
            if start_x == r - 2 and start_y == c - 2:
                uygulama.uygulama.surefinish(uyg)
                uygulama.uygulama.matrixwriter(uyg,matrix)
                print('Robot find way')
                return []
        list = self.samelistobjectdelete(list, start_x, start_y)
        return [matrix, list, start_x, start_y]

    def startformaze1(self, r, c):
        for i in range(r):
            for j in range(c):
                self.labellist[(i * c) + j].config(background='gray')
                self.matrix[i][j].blur = 1
        a = self.createstartfinishformaze1(r, c)
        return a
        # return [self.robotroadfoundformaze1(a[0], a[1], a[2], a[3], r, c),a]

    def robotroadfoundformaze1(self, start_x, start_y, finish_x, finish_y, row, column, button,buton_2,uyg,list=[],h=0):
        ustengel = 0
        altengel = 0
        sagengel = 0
        solengel = 0
        def finish():
            print()
        self.matrix[start_x][start_y].visited = 1;
        self.matrix[start_x][start_y].blockcount += 1;
        list = self.samelistobjectdelete(list,start_x,start_y)
        self.labellist[((start_x) * column) + start_y].config(background='purple')

        if start_x==finish_x and start_y==finish_y:
            print('congrats you find the finish')
            print('Congrats')
            button.config(command=finish, text='Finish')
            uygulama.uygulama.surefinish(uyg)
            uygulama.uygulama.matrixwriter(uyg,self.matrix)
            return 0
        if start_y<column-1:
            if self.matrix[start_x][start_y + 1].blocksize == 0 and self.matrix[start_x][start_y + 1].visited == 0:
                self.labellist[(start_x * column) + start_y + 1].config(background='white')
                self.matrix[start_x][start_y + 1].blur = 0
            else:
                if self.matrix[start_x][start_y + 1].visited == 1:
                    self.labellist[(start_x * column) + start_y + 1].config(background='aqua')
                else:
                    self.labellist[(start_x * column) + start_y + 1].config(background='black')
                self.matrix[start_x][start_y + 1].blur = 0
                sagengel = 1
        if start_y>0:
            if self.matrix[start_x][start_y - 1].blocksize == 0 and self.matrix[start_x][start_y - 1].visited == 0:
                self.labellist[(start_x * column) + start_y - 1].config(background='white')
                self.matrix[start_x][start_y - 1].blur = 0
            else:
                if self.matrix[start_x][start_y - 1].visited == 1:
                    self.labellist[(start_x * column) + start_y - 1].config(background='aqua')
                else:
                    self.labellist[(start_x * column) + start_y - 1].config(background='black')
                self.matrix[start_x][start_y - 1].blur = 0
                solengel = 1
        if start_x<row-1:
            if self.matrix[start_x + 1][start_y].blocksize == 0 and self.matrix[start_x + 1][start_y].visited == 0:
                self.labellist[((start_x + 1) * column) + start_y].config(background='white')
                self.matrix[start_x + 1][start_y].blur = 0
            else:
                if  self.matrix[start_x + 1][start_y].visited == 1:
                    self.labellist[((start_x + 1) * column) + start_y].config(background='aqua')
                else:
                    self.labellist[((start_x + 1) * column) + start_y].config(background='black')
                self.matrix[start_x + 1][start_y].blur = 0
                altengel = 1
        if start_x>0:
            if self.matrix[start_x - 1][start_y].blocksize == 0 and self.matrix[start_x - 1][start_y].visited == 0:
                self.labellist[((start_x - 1) * column) + start_y].config(background='white')
                self.matrix[start_x - 1][start_y].blur = 0
            else:
                if self.matrix[start_x - 1][start_y].visited == 1:
                    self.labellist[((start_x - 1) * column) + start_y].config(background='aqua')
                else:
                    self.labellist[((start_x - 1) * column) + start_y].config(background='black')
                self.matrix[start_x - 1][start_y].blur = 0
                ustengel = 1

        gecici = [sagengel, altengel, solengel, ustengel]
        #print(gecici)
        while True:
            rand = randint(0, 4)
            if gecici[rand] == 0:
                if rand == 0:
                    start_y += 1
                elif rand == 1:
                    start_x += 1
                elif rand == 2:
                    start_y -= 1
                else:
                    start_x -= 1
                break
            else:
                if gecici[0] == 1 and gecici[1] == 1 and gecici[2] == 1 and gecici[3] == 1:
                    a = self.return_new_dot(list)
                    if start_x>-1 and start_y>-1:
                        self.labellist[((start_x) * column) + start_y].config(background='aqua')
                    start_x=a[0]
                    start_y=a[1]
                    self.matrix[start_x][start_y].cantreturn=1
                    break
                else:
                    continue

        if start_x==row:
            a = self.return_new_dot(list)
            start_x = a[0]
            start_y = a[1]
            self.matrix[start_x][start_y].cantreturn = 1
        elif start_x==-1:
            a = self.return_new_dot(list)
            start_x = a[0]
            start_y = a[1]
            self.matrix[start_x][start_y].cantreturn = 1
        if start_y==column:
            a = self.return_new_dot(list)
            start_x = a[0]
            start_y = a[1]
            self.matrix[start_x][start_y].cantreturn = 1
        elif start_y ==-1:
            a = self.return_new_dot(list)
            start_x = a[0]
            start_y = a[1]
            self.matrix[start_x][start_y].cantreturn = 1
        #self.labellist[((start_x) * column) + start_y].config(background='purple')
        def stepbystep(h=0):
            self.robotroadfoundformaze1(start_x, start_y, finish_x, finish_y, row, column, button,buton_2,uyg,list,h)
        buton_2.config(command=stepbystep)
        def finish():
            button.config(command=stepbystep(1))
        if h==0:
            button.config(command=finish)
        else:
            button.config(command=stepbystep(1))


    def robotroadfoundformaze1closer(self, start_x, start_y, finish_x, finish_y, row, column):
        for  i in self.matrix:
            for j in i:
                j.visited=0
        while True:
            a = 0
            b = 0
            c = 0
            d = 0
            deneme = 0
            ustengel = 0
            altengel = 0
            sagengel = 0
            solengel = 0

            if start_x == row:
                a = 1
            elif start_y == column:
                b = 1
            elif start_x == 0:
                c = 1
            elif start_y == 0:
                d = 1

            if self.matrix[start_x + 1][start_y].blocksize == 0 and a != 1:
                a = self.closerdotfinder(start_x + 1, start_y, finish_x, finish_y)
            elif self.matrix[start_x + 1][start_y].blocksize == 0 and a == 1:
                print()
            else:
                altengel = 1

            if self.matrix[start_x][start_y + 1].blocksize == 0 and b != 1:
                b = self.closerdotfinder(start_x, start_y + 1, finish_x, finish_y)
            elif self.matrix[start_x][start_y + 1].blocksize == 0 and b == 1:
                print()
            else:
                sagengel = 1

            if self.matrix[start_x - 1][start_y].blocksize == 0 and c != 1:
                c = self.closerdotfinder(start_x - 1, start_y, finish_x, finish_y)
            elif self.matrix[start_x - 1][start_y].blocksize == 0 and c == 1:
                print()
            else:
                ustengel = 1

            if self.matrix[start_x][start_y - 1].blocksize == 0 and d != 1:
                d = self.closerdotfinder(start_x, start_y - 1, finish_x, finish_y)
            elif self.matrix[start_x][start_y - 1].blocksize == 0 and d == 1:
                print()
            else:
                solengel = 1

            self.labellist[((start_x) * column) + start_y].config(background='red')
            self.matrix[start_x][start_y].visited = 1

            if start_x == finish_x and start_y == finish_y:
                print('Congrats')
                return 0

            if altengel == 0 and solengel == 0 and sagengel == 0 and ustengel == 0:
                print(0)
                if a < b and a < c and a < d:
                    start_x += 1
                elif b < a and b < c and b < d:
                    start_y += 1
                elif c < a and c < b and c < d:
                    start_x -= 1
                elif d < a and d < b and d < c:
                    start_y -= 1
                else:
                    if a == b and self.matrix[start_x + 1][start_y].visited == 0:
                        start_x += 1
                    elif a == d and self.matrix[start_x][start_y - 1].visited == 0:
                        start_y -= 1
                    elif b == c and self.matrix[start_x][start_y + 1].visited == 0:
                        start_y += 1
                    elif d == c and self.matrix[start_x - 1][start_y].visited == 0:
                        start_x -= 1
                    elif a == c and self.matrix[start_x - 1][start_y].visited == 0:
                        start_x -= 1
                    else:
                        deneme = 1
                    print('engelsiz')
            if altengel == 1 and ustengel == 1:
                print(5)
                if b < d and self.matrix[start_x][start_y + 1].visited == 0:
                    start_y += 1
                elif d < b and self.matrix[start_x][start_y - 1].visited == 0:
                    start_y -= 1
                else:
                    if b == c and self.matrix[start_x][start_y + 1].visited == 0:
                        start_y += 1
                    else:
                        start_y -= 1
                    print('altustengel')
            if solengel == 1 and sagengel == 1:
                print(0)
                if a < c:
                    start_x += 1
                elif c < a:
                    start_x -= 1
                else:
                    print('engelsiz')
            if altengel == 1:
                 #eğer uzaklık eşitse git gel yapıyorrrrrrrrr
                print(1)
                if b < c and b < d:
                    start_y += 1
                elif c < b and c < d:
                    start_x -= 1
                elif d < b and d < c:
                    start_y -= 1
                else:
                    if (b == c and self.matrix[start_x][start_y + 1].visited == 0) or (
                            b == d and self.matrix[start_x][start_y + 1].visited == 0):
                        start_y += 1
                    elif d == c and self.matrix[start_x - 1][start_y].visited == 0:
                        start_x -= 1
                    elif d == b and self.matrix[start_x][start_y - 1].visited == 0:
                        start_y -= 1
                    else:
                        if ustengel==1 or solengel==1 or sagengel==1:
                            ustengel=0
                            solengel=0
                            sagengel=0
                        deneme = 1
                    print('altengel')
            if sagengel == 1:
                print(2)
                if a < c and a < d:
                    start_x += 1
                elif c < a and c < d and self.matrix[start_x - 1][
                    start_y].visited == 0:  # işu sikik koşul eklenecek hepsine
                    start_x -= 1
                elif d < a and d < c:
                    start_y -= 1
                else:
                    if a == d and self.matrix[start_x][start_y - 1].visited == 0:
                        start_y -= 1
                    elif d == c and self.matrix[start_x - 1][start_y].visited == 0:
                        print('sakjfgsahjf', self.matrix[start_x - 1][start_y].visited)
                        start_x -= 1
                    elif a == c and self.matrix[start_x + 1][start_y].visited == 0:
                        start_x += 1
                    else:
                        if solengel==1 or ustengel==1:
                            ustengel=0
                            solengel=0
                        deneme = 1
                    print('sağengel')
            if ustengel == 1:
                print(3)
                if a < b and a < d:
                    start_x += 1
                elif b < a and b < d:
                    start_y += 1
                elif d < a and d < b:
                    start_y -= 1
                else:
                    if a == b and self.matrix[start_x + 1][start_y].visited == 0:
                        start_x += 1
                    elif a == d and self.matrix[start_x][start_y - 1].visited == 0:
                        start_y -= 1
                    elif b == d and self.matrix[start_x][start_y + 1].visited == 0:
                        start_y += 1
                    else:
                        if solengel==1:
                            solengel=0
                        deneme = 1
                    print('ustengel')

            if solengel == 1:
                print('4')
                if a < b and a < c:
                    start_x += 1
                elif b < a and b < c:
                    start_y += 1
                elif c < a and c < b:
                    start_x -= 1
                else:
                    if a == b and self.matrix[start_x + 1][start_y].visited == 0:
                        start_x += 1
                    elif b == c and self.matrix[start_x][start_y + 1].visited == 0:
                        start_y += 1
                    elif c == a and self.matrix[start_x - 1][start_y].visited == 0:
                        start_x -= 1
                    else:
                        deneme = 1
                    print('solengel')

            print(a, b, c, d)
            if deneme == 1:
                if self.matrix[start_x + 1][start_y].visited == 0 and self.matrix[start_x + 1][start_y].blocksize == 0:
                    start_x += 1
                elif self.matrix[start_x - 1][start_y].visited == 0 and self.matrix[start_x - 1][start_y].blocksize == 0:
                    start_x -= 1
                elif self.matrix[start_x][start_y - 1].visited == 0 and self.matrix[start_x][start_y - 1].blocksize == 0:
                    start_y -= 1
                elif self.matrix[start_x][start_y + 1].visited == 0 and self.matrix[start_x][start_y + 1].blocksize == 0:
                    start_y += 1



        # return [start_x,start_y]
        
        # 1 sağ alt yapma fonksiyonu
        # 2 sol alt
        # 3 sol üst yapma fonksiyonu
        # 4 sağ üst
        # 5 sağ#
        # 6 sol
        # 7 alt
        # 8 üst
        #if start_x - finish_x > 0 and start_y - finish_y > 0:
        #    a = 3
        #elif start_x-finish_x > 0 and start_y-finish_y < 0:
        #    a=0

    def createstartfinishformaze1(self, r, c):
        while True:
            start_x = random.randint(1, r - 2)
            start_y = random.randint(1, c - 2)
            finish_x = random.randint(1, r - 2)
            finish_y = random.randint(1, c - 2)
            # start_x = 6
            # start_y = 7
            # finish_x = 7
            # finish_y = 12
            if self.matrix[start_x][start_y].blocksize == 0 and self.matrix[finish_x][finish_y].blocksize == 0:
                self.labellist[(start_x * c) + start_y].config(background='blue', text='S')
                self.labellist[(finish_x * c) + finish_y].config(background='red', text='F')
                break

        return [start_x, start_y, finish_x, finish_y]


    def closerdotfinder(self, s_x, s_y, f_x, f_y):
        s_x += 1
        s_y += 1
        f_x += 1
        f_y += 1
        return (s_x - f_x) ** 2 + (s_y - f_y) ** 2
    def return_new_dot(self,list):
        i=0
        while i<10000:
            rand = randint(0, len(list) - 1)
            start_x = list[rand][0]
            start_y = list[rand][1]
            if self.matrix[start_x][start_y].cantreturn == 0:
                return [start_x, start_y]
            else:
                i+=1


    def samelistobjectdelete(self, list, x, y):
        a = len(list)
        i = 0
        counter = 0
        while i < a:
            if list[i][0] == x and list[i][1] == y:
                counter += 1
            i += 1
        if counter == 0:
            b = [x, y]
            list.append(b)
            return list
        else:
            return list


def robotsteps(x, r, c, rbots,uyg):
    if len(x)==0:
        return x
    x = robot.robotstepsroadfound(rbots, r=r, c=c, start_x=x[2], start_y=x[3], list=x[1], matrix=x[0],uyg=uyg)
    return x
