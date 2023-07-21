from tkinter import *
from labirent import *
import tkinter as kaynak

window = Tk()
window.title("Matrix")
window.geometry("400x400+120+120")
window.configure(bg='gray')

m1 = StringVar()

matrix = []

target_url = "http://bilgisayar.kocaeli.edu.tr/prolab2/url1.txt"
y2=None
def labirent2():
    matrix = []
    window.withdraw()
    R=int(row.get())
    C=int(column.get())
    #R = 20
    #C = 25
    newWindow = Toplevel(window)
    newWindow.title("Matrix")
    newWindow.geometry("800x800+120+120")
    newWindow.configure(bg='gray')
    y2=lab.problem2maze(newWindow, matrix, R, C, kaynak)
    kaynak.Button(newWindow, text='değiştir', bg='white', fg='gray', font='verdana 17 bold', command=labirent2).place(x=250, y=y2+40)

def labirent1():
    window.withdraw()
    newWindow = Toplevel(window)
    newWindow.title("Matrix")
    newWindow.geometry("600x600+120+120")
    newWindow.configure(bg='#F5ECC1')
    lab.problem1maze(newWindow,kaynak,target_url)

label = Label(background='white',fg='black', text='lütfen satır ve sutunu sırası ile giriniz:' )
label.place(x=40,y=100)

row=Entry(window)
row.pack(pady=20)
row.place(x=250,y=100)
column=Entry(window)
column.pack(padx=20)
column.place(x=350,y=100)

kaynak.Button(window,width=25,height=10, background='white', text='Labirent 1', command=labirent1).place(x=40, y=150)
kaynak.Button(window,width=25,height=10, background='white', text='Labirent 2', command=labirent2).place(x=250, y=150)

# kaynak.Button(text='değiştir', bg='white', fg='gray', font='verdana 17 bold', command=change).place(x=500,y=800)
# buton_1 = kaynak.Button(text='Başla', bg='white', fg='gray', font='verdana 17 bold', command=startbutton)


window.mainloop()
