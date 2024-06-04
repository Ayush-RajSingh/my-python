from tkinter import *
from pymysql import *
from tkinter import messagebox

class GuiApp:
    def __init__(self) :
        self.t=Tk()
        self.t.wm_title("Student Data")
        self.t.geometry("800x500")
        #self.t.state("zoomed")
       
        
        self.lblname=Label(master=self.t,
                                        text="Roll No = ",
                                        font=("consolas",20,"bold"),fg='red')

        self.lblname.place(x=50,y=20,width=200,height=30)

        self.enrno = Entry(master=self.t,fg = 'blue',font=('consolas',15,'bold'))
        self.enrno.place(x=230,y=20,width=200,height=30)

        self.lblname=Label(master=self.t,
                                        text="Name = ",
                                        font=("consolas",20,"bold"),
                                        fg='red')

        self.lblname.place(x=50,y=60,width=200,height=30)

        self.enname = Entry(master=self.t,fg = 'blue',font=('consolas',15,'bold'))
        self.enname.place(x=230,y=60,width=200,height=30)

        self.lblcourse=Label(master=self.t,
                                        text="Course = ",
                                        font=("consolas",20,"bold"),fg='red')

        self.lblcourse.place(x=50,y=100,width=200,height=30)

        self.encourse = Entry(master=self.t,fg = 'blue',font=('consolas',15,'bold'))
        self.encourse.place(x=230,y=100,width=200,height=30)

        self.lblfees=Label(master=self.t,
                                        text="Fees = ",
                                        font=("consolas",20,"bold"),fg='red')

        self.lblfees.place(x=50,y=140,width=200,height=30)

        self.enfees = Entry(master=self.t,fg = 'blue',font=('consolas',15,'bold'))
        self.enfees.place(x=230,y=140,width=200,height=30)

        self.btnsubmit = Button(master=self.t,text= " First ",
                                font = ("consolas",20,'bold'),fg='red',
                                command=self.t)

        self.btnnext = Button(master=self.t,text= " Next ",
                                font = ("consolas",20,'bold'),fg='red',
                                command=self.next)

        self.btnnext.place(x = 150,y = 180,width=100,height=30)

        self.btnsubmit.place(x = 20,y = 180,width=100,height=30)

        self.btnpre = Button(master=self.t,text=  "Previous",
                                font = ("consolas",20,'bold'),fg='red',
                                command=self.prev)

        self.btnpre.place(x = 270,y = 180,width=150,height=30)
        self.btnlast = Button(master=self.t,text= " last ",
                                font = ("consolas",20,'bold'),fg='red',
                                command=self.t)

        self.btnlast.place(x = 450,y = 180,width=100,height=30)
        self.btnnew = Button(master=self.t,text= " New ",
                                font = ("consolas",20,'bold'),fg='red',
                                command=self.t)

        self.btnnew.place(x = 20,y = 220,width=100,height=30)
        self.btinsert = Button(master=self.t,text= " Insert ",
                                font = ("consolas",20,'bold'),fg='red',
                                command=self.t)

        self.btinsert.place(x = 150,y = 220,width=100,height=30)
        self.btupdate = Button(master=self.t,text= " Update ",
                                font = ("consolas",20,'bold'),fg='red',
                                command=self.t)

        self.btupdate.place(x = 270,y = 220,width=100,height=30)
        self.btdelete = Button(master=self.t,text= " Delete ",
                                font = ("consolas",20,'bold'),fg='red',
                                command=self.t)

        self.btdelete.place(x = 400,y = 220,width=100,height=30)
        
        self.connectToDb()

        self.t.mainloop()

    def connectToDb(self):

        self.row = 0
        
        #connection string 
        self.conn = connect(host = 'localhost',
                           user = 'root@localhost',
                           password = 'your_password',
                           db = 'sdb2')
        #connect to db
        self.cur = self.conn.cursor()

        self.getData()


    def getData(self):

        #executing the query
        self.cur.execute("select * from student ")

        #capturing the data 
        self.data = self.cur.fetchall()

        self.showData()


    def showData(self):

        self.clearAll()

        #display the data 
        self.enrno.insert(0, self.data[self.row][0])
        self.enname.insert(0, self.data[self.row][1])
        self.encourse.insert(0,self.data[self.row][2])
        self.enfees.insert(0, self.data[self.row][3])

    def next(self):
        self.row = self.row + 1
        self.showData()

    def prev(self):

        if(self.row == 0):
            messagebox.showwarning(self.t,"First Record")
        else:
            self.row = self.row - 1
            self.showData()
            

    def clearAll(self):
        self.encourse.delete(0,'end')
        self.enfees.delete(0,'end')
        self.enname.delete(0,'end')
        self.enrno.delete(0,'end')
    

if __name__ == '__main__':
    g = GuiApp()