from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import mysql.connector
from texttable import Texttable
#---------------------------REGISTRATION FORM-------------------------------------
class Reg:
    def __init__(self,master):
      self.master = master
      self.master.geometry("300x140+50+50")
      self.master.title("Registration Form")

      self.master.tname=Label(self.master,text="NAME")
      self.master.pname=Entry(self.master)
      self.master.tregno=Label(self.master,text="REGNO")
      self.master.pregno=Entry(self.master)
      self.master.tuser=Label(self.master,text="AGE")
      self.master.puser=Entry(self.master)
      self.master.tpass=Label(self.master,text="GENDER")
      self.master.ppass=Entry(self.master)
      self.master.tmone=Label(self.master,text="MONTHLY EXPENDITURE")
      self.master.pmone=Entry(self.master)
      self.master.b11=Button(self.master,text="SUBMIT",command=self.f2)

      self.master.b12=Button(self.master,text="EXIT",command=self.master.destroy)
      self.master.tname.grid(row=0,column=0)
      self.master.pname.grid(row=0,column=1)
      self.master.tregno.grid(row=1,column=0)
      self.master.pregno.grid(row=1,column=1)
      self.master.tuser.grid(row=2,column=0)
      self.master.puser.grid(row=2,column=1)
      self.master.tpass.grid(row=3,column=0)
      self.master.ppass.grid(row=3,column=1)
      self.master.tmone.grid(row=4,column=0)
      self.master.pmone.grid(row=4,column=1)
      self.master.b11.grid(row=5,column=0)
      self.master.b12.grid(row=5,column=1)

    def f2(self):
        try:
            mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="login"
            )

            s1=self.master.pname.get()
            s2=self.master.pregno.get()
            s3=self.master.puser.get()
            s4=self.master.ppass.get()
            s5=self.master.pmone.get()


            mycursor=mydb.cursor()
            mycursor.execute("insert into reg1 values ('"+ s1 + "' ,'"+ s2 + "' ,'" + s3 + "' ,'"+ s4 + "',' " +s5 + " ' ) ")
            mydb.commit()

            if(mycursor):
                messagebox.showinfo("info","Inserted")
                root3=Toplevel(self.master)
                exp=Exp(root3)
            else:
                messagebox.showinfo("error","not Inserted")
        except Exception as e :
            messagebox.showerror("error",str(e))

#------------------------------------------------LOGIN FORM--------------------------------------------
class Login:
        def __init__(self,master):
          self.master = master
          self.master.geometry("300x140+50+50")
          self.master.title("Login Page")
          self.uname=Label(self.master,text="Enter Username")
          self.lname=Entry(self.master)
          self.upass=Label(self.master,text="Enter Password")
          self.lpass=Entry(self.master)
          self.uname.grid(row=0)
          self.lname.grid(row=0,column=1)
          self.upass.grid(row=1)
          self.lpass.grid(row=1,column=1)
          self.b1=Button(self.master,text="Login",command=self.f2)
          self.b2=Button(self.master,text="Exit",command=self.master.destroy)
          self.b1.grid(row=2,column=0)
          self.b2.grid(row=2,column=1)

        def f2(self):
            try:
                mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="login"
                )

                self.l1=self.lname.get()
                self.l2=self.lpass.get()

                mycursor=mydb.cursor()

                mycursor.execute("select * from login1 where userid='"+ self.l1 +"' and password='" + self.l2 +"'  ")
                myresult=mycursor.fetchone()

                if(myresult):
                    root.withdraw()
                    messagebox.showinfo("info","welcome")
                    root2=Toplevel(self.master)
                    reg = Reg(root2)

                else:
                    messagebox.showinfo("error","wrong username or password")
            except Exception as e :
                messagebox.showerror("error",str(e))

class Exp:
        def __init__(self,master):
            self.master=master
            self.master.geometry("300x140+50+50")
            self.master.title("EXPENDITURE")
            self.s=IntVar()
            self.value1=["RENT","FOOD","TRAVEL","OTHERS"]
            self.l1=Label(self.master,text="SELECT EXPENDITURE TYPE")
            self.cb1=Combobox(self.master,values=self.value1)
            self.cb1.set("--SELECT--")
            self.a1=Label(self.master,text="AMOUNT")
            self.a2=Entry(self.master)
            self.a5=Label(self.master,text="TOTAL AMOUNT")
            self.a6=Entry(self.master)
            self.b1=Button(self.master,text="UPDATE",command=self.f3)
            self.b3=Button(self.master,text="SHOW DATA",command=self.f4)
            self.b2=Button(self.master,text="EXIT",command=self.master.destroy)
            self.l1.grid(row=0,column=0)
            self.cb1.grid(row=0,column=1)
            self.a1.grid(row=1,column=0)
            self.a2.grid(row=1,column=1)
            self.a5.grid(row=2,column=0)
            self.a6.grid(row=2,column=1)
            self.b1.grid(row=3,column=0)
            self.b2.grid(row=3,column=1)
            self.b3.grid(row=4,column=2)
        def f3(self):
            try:
                mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="login"
                )
                self.l1=self.cb1.get()
                self.l2=self.a2.get()
                mycursor=mydb.cursor()
                mycursor.execute("insert into exp1 values ('"+ self.l1 + "' ,'"+ self.l2 +"') ")
                mydb.commit()
            except Exception as e :
                        messagebox.showerror("error",str(e))
        def f4(self):
            try:
                mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="login")
                mycursor=mydb.cursor()
                t=Texttable()
                mycursor.execute("Select extype from exp1")
                myresult1=mycursor.fetchall()
                mycursor.execute("select amount from exp1")
                myresult2=mycursor.fetchall()
                t.add_rows([['EXPENDITURE TYPE','AMOUNT'],[myresult1,myresult2]])
                print(t.draw())
            except Exception as e :
                        messagebox.showerror("error",str(e))

root = Tk()
win1 = Login(root)
root.mainloop()


