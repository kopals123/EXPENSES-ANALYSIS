# **EXPENSES-MANAGEMENT**

##ABOUT

The  project of “MANAGING EXPENSES” is an application for students to collect information of the monthly expenses they do which gets directly fed into the database, 
so that the person can evaluate the expenses he/she made during the whole month and can manage it accordingly. 
It is an effective and economical way to keep record of all the data of the expenses as it is user friendly and stores data in the database permanently. 
He/she can review it later and can track the monthly expenses and can act accordingly.

##LANGUAGE USED

* PYTHON

##IDE USED

* JETBRAINS PYCHARM

##LOCAL SERVER USED

*WAMPSERVER

##SAMPLE CODE

```
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
```
