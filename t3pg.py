from tkinter import *
from PIL import ImageTk,Image
import mysql.connector as c
import tkinter.messagebox as tmsg
from tkinter import ttk
import ttkbootstrap as tkb
from ttkbootstrap.scrolled import ScrolledFrame
#from sql_th import sqlps


n='mohar466'

def thpg():
    self=Tk()
    self.geometry('1200x700')
    self.title('ACCOUNT INFORMATION')
    hu = Image.open('7.jpg')
    tu = hu.resize((1366, 768))
    jl = ImageTk.PhotoImage(tu)
    Label(self, image=jl, bg='gray71').place(relwidth=1, relheight=1)
    mynote=ttk.Notebook(self)
    mynote.pack(fill=BOTH,padx=70,pady=50)

    f1=Frame(mynote,width=1200,height=700,bg='gray99')
    f1.pack(fill=BOTH,side=LEFT)

    t3 = Image.open('8.jpg')
    t4 = t3.resize((436, 400))
    j4 = ImageTk.PhotoImage(t4)
    Label(f1, image=j4).grid(row=2, column=5, padx=45, pady=20)

    Label(f1, text='Account Information',
          activebackground='gray90', bg='grey1',
          fg='mintcream', font=('algerian 30 bold'),width=20,relief=SUNKEN).grid(row=0, column=3, padx=5,pady=5)

    f=Frame(f1,bg='grey99')
    f.grid(row=2,column=3)
    l1=Label(f,text='Name :',font=('bahnschrift_semibold 20 bold'),bg='grey99',relief=RAISED,padx=10)
    l2=Label(f,text='PAN Card Number :',font=('bahnschrift_semibold 20 bold'),relief=RAISED,padx=10,bg='grey99')
    l3=Label(f,text='Adhaar Card Number :',font=('bahnschrift_semibold 20 bold'),relief=RAISED,padx=10,bg='grey99')
    l4=Label(f,text='Phone Number :',font=('bahnschrift_semibold 20 bold'),relief=RAISED,padx=10,bg='grey99')
    l5=Label(f,text='Address :',font=('bahnschrift_semibold 20 bold'),relief=RAISED,padx=10,bg='grey99')

    i1 = StringVar()
    i2 = StringVar()
    i3 = StringVar()
    i4 = StringVar()
    i5 = StringVar()

    i1s=Entry(f,textvariable=i1,font=('20'),bg='grey71',width=50)
    i2s=Entry(f,textvariable=i2,font=('20'),bg='grey71',width=50)
    i3s=Entry(f,textvariable=i3,font=('20'),bg='grey71',width=50)
    i4s=Entry(f,textvariable=i4,font=('20'),bg='grey71',width=50)
    i5s=Entry(f,textvariable=i5,font=('20'),bg='grey71',width=50)

    l1.pack(side=TOP,anchor='w')
    i1s.pack(side=TOP,anchor='w',pady=10)

    l2.pack(side=TOP,anchor='w')
    i2s.pack(side=TOP,anchor='w',pady=10)

    l3.pack(side=TOP,anchor='w')
    i3s.pack(side=TOP,anchor='w',pady=10)

    l4.pack(side=TOP,anchor='w')
    i4s.pack(side=TOP,anchor='w',pady=10)

    l5.pack(side=TOP,anchor='w')
    i5s.pack(side=TOP,anchor='w',pady=10)



    def open():
        try:
            '''i = c.connect(host='localhost', username='root', passwd=n, database='info')
            if i.is_connected():
                print('succesful')
                cur = i.cursor()
                h = "insert into account(name,pan,aadhar,phone,adress) values('{}','{}','{}','{}','{}')".format(str(i1s.get()), str(i2s.get()),
                                                                                  str(i3s.get()), i4s.get(), str(i5s.get()))
                cur.execute(h)
                i.commit()'''
            #n=sqlps()
            f0 = Frame(mynote, width=1210, height=700, bg='grey99')
            f0.pack(side=LEFT, fill=BOTH)
            mynote.add(f0, text='Bank Info')
            self.p1 = Image.open('9.jpg')
            self.p2 = self.p1.resize((436, 400))
            self.p3 = ImageTk.PhotoImage(self.p2)
            Label(f0, image=self.p3).grid(row=2, column=5, padx=30, pady=20)
            self.p4 = Image.open('10.jpg')
            self.p5 = self.p4.resize((436, 100))
            self.p6 = ImageTk.PhotoImage(self.p5)
            Label(f0, image=self.p6).grid(row=0, column=5, padx=30, pady=20)
            Label(f0, text='Bank Account Information',
              activebackground='gray90', bg='grey1',
              fg='mintcream', font=('algerian 25 bold'),width=25,height=2,relief=SUNKEN).grid(row=0, column=3, padx=5,pady=3)
            f5=Frame(f0,bg='grey99')
            f5.grid(row=2,column=3)
            l6=Label(f5,text='Name of Bank :',font=('bahnschrift_semibold 20 bold'),bg='grey99',relief=RAISED,padx=10)
            l7=Label(f5,text='Account Number :',font=('bahnschrift_semibold 20 bold'),relief=RAISED,padx=10,bg='grey99')
            l8=Label(f5,text='Type Of Account :',font=('bahnschrift_semibold 20 bold'),relief=RAISED,padx=10,bg='grey99')
            l9=Label(f5,text='IFSC Code :',font=('bahnschrift_semibold 20 bold'),relief=RAISED,padx=10,bg='grey99')

            global j1s

            j1 = StringVar()
            j2 = StringVar()
            j3 = StringVar()
            j4 = StringVar()


            j1s = Entry(f5, textvariable=j1, font=('20'), bg='grey71', width=50)
            j2s = Entry(f5, textvariable=j2, font=('20'), bg='grey71', width=50)
            j3s = Entry(f5, textvariable=j3, font=('20'), bg='grey71', width=50)
            j4s = Entry(f5, textvariable=j4, font=('20'), bg='grey71', width=50)
            l6.pack(side=TOP, anchor='w')
            j1s.pack(side=TOP, anchor='w', pady=12)
            l7.pack(side=TOP, anchor='w')
            j2s.pack(side=TOP, anchor='w', pady=12)
            l8.pack(side=TOP, anchor='w')
            j3s.pack(side=TOP, anchor='w', pady=12)
            l9.pack(side=TOP, anchor='w')
            j4s.pack(side=TOP, anchor='w', pady=12)
        except:
            tmsg.showinfo('Warning','Check Phone no.')

        def close():
            i = c.connect(host='localhost', username='root', passwd=n, database='info')
            if i.is_connected():
                # print('succesful')
                cur = i.cursor()
                k = "insert into bank_info(name_of_bank,acc_no,type_of_acc,ifsc) values('{}','{}','{}','{}')".format(
                    str(j1s.get()), str(j2s.get()), str(j3s.get()), str(j4s.get()))
                h = "insert into account(name,pan,aadhar,phone,adress) values('{}','{}','{}','{}','{}')".format(
                    str(i1s.get()), str(i2s.get()),
                    str(i3s.get()), i4s.get(), str(i5s.get()))
                cur.execute(h)

                cur.execute(k)
                i.commit()
            #todo:third page


            fc =Frame(mynote, width=1210, height=700,bg="grey99")
            fc.pack(side=LEFT, fill=BOTH)
            mynote.add(fc, text='DETAILS VIEW')
            Label(fc,text='FINAL DOCUMENT',font=('baskerville_old_face 40 bold'),bg='grey99').grid(row=0,column=2)
            lc1 = Label(fc, text='Name :', font=('bahnschrift_semibold 20 bold'), bg='grey99',  padx=10)
            lc2 = Label(fc, text='PAN Card Number :', font=('bahnschrift_semibold 20 bold'),  padx=10,
                       bg='grey99')
            lc3 = Label(fc, text='Adhaar Card Number :', font=('bahnschrift_semibold 20 bold'),  padx=10,
                       bg='grey99')
            lc4 = Label(fc, text='Phone Number :', font=('bahnschrift_semibold 20 bold'),  padx=10,
                       bg='grey99')
            lc5 = Label(fc, text='Address :', font=('bahnschrift_semibold 20 bold'),  padx=10, bg='grey99')
            lc6 = Label(fc, text='Name of Bank :', font=('bahnschrift_semibold 20 bold'), bg='grey99',
                       padx=10)
            lc7 = Label(fc, text='Account Number :', font=('bahnschrift_semibold 20 bold'), padx=10,
                       bg='grey99')
            lc8 = Label(fc, text='Type Of Account :', font=('bahnschrift_semibold 20 bold'), padx=10,
                       bg='grey99')
            lc9 = Label(fc, text='IFSC Code :', font=('bahnschrift_semibold 20 bold'), padx=10,
                       bg='grey99')
            lol=[lc1,lc2,lc3,lc4,lc5,lc6,lc7,lc8,lc9]
            for e in range(0,9) :
                lol[e].grid(row=e+1,column=1,sticky=W)

            lol1=[i1s.get(),i2s.get(),i3s.get(),i4s.get(),i5s.get(),j1s.get(),j2s.get(),j3s.get(),j4s.get()]
            for i in range(0,9):
                Label(fc,text=lol1[i],font=('arial_narrow 20 bold'),bg='grey99',pady=10).grid(row=i+1,column=3,sticky=W)
                Label(fc,text=':',font=('bahnschrift_semibold 20 bold'),bg='grey99',pady=10).grid(row=i+1,column=2,sticky=E)



        Button(f0, text="NEXT", command=close, background='gray32', font=('20'), relief=RAISED, height=1, width=5).grid(
            row=2, column=4)
    Button(f1, text="NEXT",background='gray32',font=('20'),relief=RAISED, command=open,height=1,width=5).grid(row=3, column=4)
    mynote.add(f1,text='Account Info')
    self.mainloop()


thpg()
