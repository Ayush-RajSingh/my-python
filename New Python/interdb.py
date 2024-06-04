from tkinter import *
from pymysql import *
from tkinter import messagebox

def connectToDb():
    row = 0
    conn = connect(host = 'localhost',
                        user = 'root',
                        password = '',
                        db = 'sdb2')    
    curs = conn.cursor()

    getData()

def getData():
    cur.execute("select * from student ") 
data = cur.fetchall()

def showData():

    clearAll()
    t1.insert(0,data[row][0])
    t2.insert(0,data[row][1])
    t3.insert(0,data[row][2])
    t4.insert(0,data[row][3])

def next():
    row = row + 1

def prev():

    if(row == 0):
        messagebox.showwarning(win,"First Record")
    else:
        row = row - 1

def clearAll():
    t1.delete(0,'end')
    t2.delete(0,'end')
    t3.delete(0,'end')
    t4.delete(0,'end')


win=Tk()
win.title('sql database')
win.geometry("850x500")
label1=Label(win, text='Roll no.')    
label2=Label(win, text='Name')
label3=Label(win, text='Course')
label4=Label(win, text='Fees')
t1= Entry(bd=3)
t2=Entry(bd=3)
t3= Entry(bd=3)
t4=Entry(bd=3)

label1.place(x=100, y=50)
t1.place(x=200, y=50)
label2.place(x=100, y=100)
t2.place(x=200, y=100)
label3.place(x=100, y=150)
t3.place(x=200, y=150)
label4.place(x=100, y=200)
t4=Entry(bd=3)

b1=Button(win, text='First', )
b2=Button(win, text='Next', )
b3=Button(win, text='prev',)
b4=Button(win, text='last',)
b5=Button(win, text='new', )
b6=Button(win, text='insert', )
b7=Button(win, text='update', )
b8=Button(win, text='delete', )
b1.place(x=100, y=230)
b2.place(x=160, y=230)
b3.place(x=220, y=230)
b4.place(x=280, y=230)
b5.place(x=100, y=260)
b6.place(x=160, y=260)
b7.place(x=220, y=260)
b8.place(x=280, y=260)

connectToDb()
win.mainloop()
