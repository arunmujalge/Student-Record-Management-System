from tkinter import *
from tkinter import ttk
import tkinter

import mysql.connector as sql

top = tkinter.Tk()
top.geometry("1000x2000")
l= Label(top,text ="student record management",font=('arial',40),fg='red')
l.grid(row=0,column=1)

l1= Label(top,text =" student id:",font=('arial',30),fg='black',)
l1.grid(row=1,column=0)
E1 = Entry(top,bd=5,width=50,)
E1.grid(row=1,column= 1)

l2= Label(top,text =" student name:",font=('arial',30),fg='black',)
l2.grid(row=2,column=0)
E2 = Entry(top,bd=5,width=50,)
E2.grid(row=2,column= 1)

l3= Label(top,text =" student gender:",font=('arial',30),fg='black',)
l3.grid(row=3,column=0)
E3 = Entry(top,bd=5,width=50,)
E3.grid(row=3,column= 1)

l4= Label(top,text ="  student email:",font=('arial',30),fg='black',)
l4.grid(row=4,column=0)
E4 = Entry(top,bd=5,width=50)
E4.grid(row=4,column= 1)

l5= Label(top,text ="  student contact:",font=('arial',30),fg='black',)
l5.grid(row=5,column=0)
E5 = Entry(top,bd=5,width=50)
E5.grid(row=5,column= 1)

l6= Label(top,text ="  student DOB:",font=('arial',30),fg='black',)
l6.grid(row=6,column=0)
E6 = Entry(top,bd=5,width=50)
E6.grid(row=6,column= 1)

l7= Label(top,text ="  student address:",font=('arial',30),fg='black',)
l7.grid(row=7,column=0)
E7 = Entry(top,bd=5,width=50)
E7.grid(row=7,column= 1)


frm=Frame(top)
frm.grid(row=11,column=1,)
table=ttk.Treeview(frm,column=(1,2,3,4,5,6,7),show="headings",height="9",)
yscrollbar=ttk.Scrollbar(frm,orient='vertical',command=table.yview())
table.configure(yscroll=yscrollbar.set)
table.grid(row=11,column=1,)
yscrollbar.grid(row=11,column=2,sticky="ns")
table.heading(1,text="id")
table.column(1, width=40)
table.heading(2,text="name")
table.heading(3,text="gender")
table.column(3, width=60)
table.heading(4,text="email")
table.heading(5,text="contact")
table.heading(6,text="DOB")
table.heading(7,text="address")




def buttonevent(selection):
    print("student id ",E1.get())
    print("student name ", E2.get())
    print("student gender ", E3.get())
    print("student email",E4.get())
    print("student contact ", E5.get())
    print("student DOB", E6.get())
    print("student address", E7.get())
    id=E1.get()
    name=E2.get()
    gender= E3.get()
    email=E4.get()
    contact=E5.get()
    DOB=E6.get()
    address=E7.get()
    if selection in ('INSERT'):
        mycon = sql.connect(host='localhost', user='root', password='Arun@123456', database='project')
        cur =mycon.cursor()
        for record in table.get_children():
         table.delete(record)
        q="select * from  record order by ID"

        query="create table if not exists record(ID varchar(20) Not null,NAME varchar(20), GENDER varchar(30),EMAIL varchar(100),CONTACT varchar(30),DOB varchar (30),ADDRESS varchar(30))"

        cur.execute(query)

        mycon.commit()
        print("table record created ")

        inquery="insert into record (ID,NAME,GENDER,EMAIL,CONTACT,DOB,ADDRESS) values ('%s','%s','%s','%s','%s','%s','%s' )"%(id,name,gender,email,contact,DOB,address)
        cur.execute(inquery)
        cur.execute(q)
        rows = cur.fetchall()
        for i in rows:
            table.insert('', 'end', values=i)

        E1.delete(0, END)
        E2.delete(0, END)
        E3.delete(0, END)
        E4.delete(0, END)
        E5.delete(0, END)
        E6.delete(0, END)
        E7.delete(0, END)

        mycon.commit()
        mycon.close()
    elif selection in ('UPDATE'):
        qshow = "SELECT * from record  where ID ='%s'" % (id)
        for record in table.get_children():
            table.delete(record)
        qupdate ="update record set NAME='%s'"% (name) +",GENDER='%s'"% (gender)+",EMAIL='%s'"% (email)+",CONTACT='%s'"% (contact)+",DOB='%s'"%(DOB)+",ADDRESS='%s'"%(address)+"where ID ='%s'"%(id)
        mycon = sql.connect(host='localhost', user='root', password='Arun@123456', database='project')
        cur = mycon.cursor()
        for record in table.get_children():
            table.delete(record)


        cur.execute(qupdate)
        cur.execute(qshow)
        rows = cur.fetchall()

        for i in rows:
            table.insert('', 'end', values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        E1.delete(0, END)
        E2.delete(0, END)
        E3.delete(0, END)
        E4.delete(0, END)
        E5.delete(0, END)
        E6.delete(0, END)
        E7.delete(0, END)

        mycon.commit()
        mycon.close()
    elif selection in ('DELETE'):
        q = "select * from record order by ID"
        qdelete ="delete from record  where ID ='%s'"%(id)
        for record in table.get_children():
            table.delete(record)
        mycon = sql.connect(host='localhost', user='root', password='Arun@123456', database='project')
        cur = mycon.cursor()
        cur.execute(qdelete)
        cur.execute(q)
        rows = cur.fetchall()

        for i in rows:
            table.insert('', 'end', values=(i))
        mycon.commit()
        mycon.close()

    elif selection in ('SEARCH'):
        qsearch ="SELECT * from record  where ID ='%s'"%(id)
        for record in table.get_children():
            table.delete(record)
        mycon = sql.connect(host='localhost', user='root', password='Arun@123456', database='project')
        cur = mycon.cursor()
        cur.execute(qsearch)
        rows =cur.fetchall()


        for i in rows:
            table.insert('', 'end', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

        mycon.close()
    elif selection in ('SHOWALL'):
        qshowall= "SELECT * from record order by ID"
        for record in table.get_children():
            table.delete(record)
        mycon = sql.connect(host='localhost', user='root', password='Arun@123456', database='project')
        cur = mycon.cursor()
        cur.execute(qshowall)
        rows = cur.fetchall()

        for i in rows:
            table.insert('', 'end', values=(i))

        mycon.close()

Binsert=tkinter.Button(top,text='INSERT',fg='black',font=('arial',20),command=lambda:buttonevent('INSERT'))
Binsert.grid(row=8 ,column=0)

Bupdate=tkinter.Button(top,text='UPDATE',fg='black',font=('arial',20),command=lambda: buttonevent('UPDATE') )
Bupdate.grid(row=8 ,column=1)

Bdelete=tkinter.Button(top,text='DELETE',fg='black',font=('arial',20),command=lambda: buttonevent('DELETE'))
Bdelete.grid(row=9 ,column=1)


Bsearch=tkinter.Button(top,text='SEARCH',fg='black',font=('arial',20),command=lambda: buttonevent('SEARCH'))
Bsearch.grid(row=9 ,column=0)

Bsearch=tkinter.Button(top,text='SHOWALL',fg='black',font=('arial',20),command=lambda: buttonevent('SHOWALL'))
Bsearch.grid(row=10 ,column=0)













top.title("student record management")

top.mainloop()
