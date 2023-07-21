import random
from block import *
from tkinter import Label


def squareblock(matrix, r, c):
    i = 0
    while (i < r):
        matrix[i][0].definitly = 1

        matrix[i][c - 1].definitly = 1

        i += 1
    i = 0
    while i < c:
        matrix[0][i].definitly = 1
        matrix[r - 1][i].definitly = 1
        i += 1
    return matrix


def allblock(matrix, R, C, width=0):
    for i in range(R):
        a = []
        for j in range(C):
            # a.append(randint(0,1))
            a.append(block(0, 0, 1, blocksize=width))
        matrix.append(a)
    return matrix


def createstartfinish(matrix, R, C):
    start_x = 1
    start_y = 0
    finish_x = R - 2
    finish_y = C - 1
    matrix[start_x][start_y] = block(1, 0, 0)
    matrix[finish_x][finish_y] = block(1, 0, 0)  # 1 -1 0
    matrix[-2][-2] = block(0, 0, 0, blur=5)
    createroad(matrix, R, C)


def createroad(matrix, R, C):
    row = 0
    column = 0
    i = 0
    a = int
    check = 0
    list = []
    while matrix[row][column].changeable != -1:
        b = random.randint(0, 3)
        if row == 0 and column == 0 and matrix[row][column - 1].changeable == 0:
            a = random.randint(0, 1)
            a = 1
            if a == 1:
                row += 1
            elif a == 0:
                column += 1

        else:
            if a == 1:
                if column == C:
                    column -= 1
                if row == R:
                    row -= 1
                if matrix[row][column + 1].blur == 5:
                    column += 1
                elif matrix[row + 1][column].blur == 5:
                    row += 1
                elif matrix[row + 1][column + 1].blur == 5:
                    gecici = random.randint(0, 1)
                    if gecici == 0:
                        column += 1
                    else:
                        row += 1


                else:

                    if b == 0 and matrix[row][column - 1].definitly == 0 and matrix[row][column - 1].changeable == 0 and \
                            (matrix[row + 1][column - 1].changeable == 0 and matrix[row - 1][
                                column - 1].changeable == 0) and \
                            matrix[row][column - 2].changeable == 0:
                        column -= 1
                    elif b == 1 and matrix[row + 1][column].definitly == 0 and matrix[row + 1][
                        column].changeable == 0 and \
                            (matrix[row + 1][column - 1].changeable == 0 and matrix[row + 1][
                                column + 1].changeable == 0) and \
                            matrix[row + 2][column].changeable == 0:
                        row += 1
                    elif b == 2 and matrix[row][column + 1].definitly == 0 and matrix[row][
                        column + 1].changeable == 0 and \
                            (matrix[row - 1][column + 1].changeable == 0 and matrix[row + 1][
                                column + 1].changeable == 0) and \
                            matrix[row][column + 2].changeable == 0:
                        column += 1
                    elif b == 3 and matrix[row - 1][column].definitly == 0 and matrix[row - 1][
                        column].changeable == 0 and \
                            (matrix[row - 1][column + 1].changeable == 0 and matrix[row - 1][
                                column - 1].changeable == 0) and \
                            matrix[row - 2][column].changeable == 0:
                        row -= 1
                    else:

                        gecici = random.randint(0, len(list) - 1)
                        if matrix[list[gecici][0]][list[gecici][1]].changeable == 1 and matrix[list[gecici][0]][
                            list[gecici][1]].cantreturn == 0:
                            check = 0
                            row = list[gecici][0]
                            column = list[gecici][1]
                            # matrix[row][column] = block(matrix[row][column].definitly,matrix[row][column].changeable,matrix[row][column].value,1)
                            matrix[row][column].cantreturn = 1


                        else:  # şu siktiğimin geri dönüp rastgele yol bulmasını çözzzzzzzzzzzzzzzz
                            # print(list[gecici])
                            if i == 10000:
                                print("bitti")
                                break
                            else:
                                i += 1

        # print(row,column,matrix[row][column].changeable)
        # print(matrix[row][column].cantreturn)
        if check == 0:
            matrix[row][column].changeable = 1  # = block(0, 1, 0)
            matrix[row][column].value = 0
            gecici = [row, column]
            if len(list) != 0:
                if gecici != list[-1]:
                    list.append(gecici)
            else:
                list.append(gecici)
        if row == R - 2 and column == C - 1:
            row = random.randint(0, R - 1)
        check = 0


def allblockformaze1(b, R, C):
    matrix = []
    for i in range(R):
        a = []
        for j in range(C):
            a.append(block(0, 0, 0, blocksize=b[i][j]))
        matrix.append(a)
    return matrix


def createroadformaze1(self, matrix, r, c):
    counter = 0
    x2 = 0
    y2 = 0
    labellist = {}
    for i in range(r):
        for j in range(c):
            if matrix[i][j].blocksize == 0 and matrix[i][j].definitly == 0 and matrix[i][j].blur == 0:
                entry = Label(self, width=3, background='white')
                labellist[counter] = entry
            elif matrix[i][j].blocksize == 1 and matrix[i][j].definitly == 0 and matrix[i][j].blur == 0:
                entry = Label(self, width=3, background='black')
                labellist[counter] = entry
            elif matrix[i][j].blocksize == 2 and matrix[i][j].definitly == 0 and matrix[i][j].blur == 0:
                rand = random.randint(0, 3)  # bura random bi şekilde şekil oluşturmada kullanılır
                rand = 10
                if rand == 0:
                    entry = Label(self, width=3, background='green')
                    matrix[i][j].blocksize = 0
                else:
                    entry = Label(self, width=3, background='black')
                labellist[counter] = entry
            elif matrix[i][j].blocksize == 3 and matrix[i][j].definitly == 0 and matrix[i][j].blur == 0:
                rand = random.randint(0, 3)  # bura random bi şekilde şekil oluşturmada kullanılır
                rand = 10
                if rand == 0:
                    entry = Label(self, width=3, background='green')
                    matrix[i][j].blocksize = 0
                else:
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

    return [labellist, y2]
