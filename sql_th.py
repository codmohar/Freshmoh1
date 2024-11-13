from tkinter import *


n='mohar466'

def sqlcon():
    import mysql.connector as con
    i = con.connect(host='localhost', user='root', passwd=n)
    cur = i.cursor()
    cur.execute("create database info")
    cur.execute('use info')
    cur.execute('create table register(username varchar(40) NOT NULL ,respas varchar(10) unique NOT NULL)')
    cur.execute('create table account(acc_pas varchar(10) unique ,name varchar(40) NOT NULL,pan varchar(10),aadhar varchar(12),phone varchar(10) primary key,adress varchar(50))')
    cur.execute('create table bank_info(ba_pass varchar(10) unique ,name_of_bank varchar(20) NOT NULL,acc_no varchar(15) REFERENCES account(phone),type_of_acc varchar(12) NOT NULL,ifsc varchar(11) primary key)')


def bank_con():
    import mysql.connector as con
    i = con.connect(host='localhost', user='root', passwd=n)
    cur = i.cursor()
    # cur.execute("create database info")
    cur.execute('use info')


def sqldes():
    import mysql.connector as con
    i = con.connect(host='localhost', user='root', passwd=n)
    cur = i.cursor()
    cur.execute("drop database info")



def sqlps():
    global rr
    self=Tk()
    self.title('GET INFO')
    Label(self,text='MYSQL Password',background='gray95').pack()
    rr=StringVar()
    r1=Entry(self,textvariable=rr)
    r1.pack()
    #Button(self,command=quit,text='Give').pack(anchor='e')
    self.mainloop()
    return rr.get()




ch=int(input(':'))

if ch==1:
    sqlcon()
elif ch==2:
    sqldes()