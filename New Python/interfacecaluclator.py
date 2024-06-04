from tkinter import *

def add():
    t3.delete(0, 'end')
    num1=float(t1.get())
    num2=float(t2.get())
    result=num1+num2
    result=round(result,4)
    t3.insert(END, str(result))
    label3.config(text="Addition")
   
def sub():
    t3.delete(0, 'end')
    num1=float(t1.get())
    num2=float(t2.get())
    result=num1-num2
    result=round(result,4)
    t3.insert(END, str(result))
    label3.config(text="Subtraction")

def mul():
    t3.delete(0, 'end')
    num1=float(t1.get())
    num2=float(t2.get())
    result=num1*num2
    result=round(result,4)
    t3.insert(END, str(result))
    label3.config(text="Multiplication")

def div():
    t3.delete(0, 'end')
    num1=float(t1.get())
    num2=float(t2.get())
    result=num1/num2
    result=round(result,4)
    t3.insert(END, str(result))
    label3.config(text="Division")

def clear_text(self):
    self.delete(0, END)

win=Tk()
win.title('Calculator')
win.geometry("850x500")

label1=Label(win, text='Number 1')
label2=Label(win, text='Number 2')
label3=Label(win, text='Result')
t1= Entry(bd=3)
t2=Entry()
t3=Entry()


label1.place(x=100, y=50)
t1.place(x=200, y=50)
label2.place(x=100, y=100)
t2.place(x=200, y=100)


b1=Button(win, text='   Add   ', command=add)
b2=Button(win, text='Subtract', command=sub)
b3=Button(win, text='Multiply', command=mul)
b4=Button(win, text='Divide', command=div)
b5=Button(win, text='Clear', command=clear_text)
b1.place(x=100, y=150)
b2.place(x=160, y=150)
b3.place(x=220, y=150)
b4.place(x=280, y=150)
b5.place(x=340, y=150)
label3.place(x=100, y=200)
t3.place(x=200, y=200)
win.mainloop()
