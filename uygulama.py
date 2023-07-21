from datetime import datetime
from tkinter import Tk, Label


class uygulama:
    def __init__(self,start, newwindow):
        self.start = start
        self.matrix=None
        self.counter=None
        self.newwindow=newwindow
        self.time_elapsed=None

    def surestart(self):
        self.start =  datetime.now()
    def surefinish(self):
        self.time_elapsed = datetime.now() - self.start
        print('{}'.format(self.time_elapsed))
    def matrixwriter(self, matrix):
        self.matrix=matrix
        counter=0
        for i in matrix:
            for j in i:
                print(j.blockcount,end=' ')
                if j.blockcount>1:
                    counter+=1
                else:
                    counter+=j.blockcount
            print()
        self.counter=counter
        print('toplam geçilen kare sayısı: ',counter)
        newWindow = Tk()
        newWindow.title("sonuç")
        newWindow.geometry("250x250+120+120")
        newWindow.configure(bg='gray')
        entry = Label(newWindow, width=30, background='white',
                      text='toplam geçilen kare sayisi: ' + str(counter))
        entry.place(x=25, y=25)
        entry = Label(newWindow, width=30, background='white',
                      text='toplam süre: ' + str(self.time_elapsed))
        entry.place(x=25, y=50)