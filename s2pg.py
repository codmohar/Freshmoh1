from tkinter import *
from PIL import ImageTk,Image
import mysql.connector as c
import tkinter.messagebox as tmsg



def por():
    #n = input('Enter sql password:')
    self=Tk()
    self.geometry("1200x700")
    self.title('REGISTRATION')
    self.iconbitmap('icon.png')
    self.l = Image.open('5.jpg')
    self.k = self.l.resize((1200, 700))
    self.jj = ImageTk.PhotoImage(self.k)
    Label(self, image=self.jj, bg='gray71').place(relwidth=1, relheight=1)

    f1 = Frame(self, bg='grey71',relief=SUNKEN, borderwidth=4)
    f2 = Frame(self, bg='grey71',relief=SUNKEN, borderwidth=2)

    f1.pack(side=TOP,padx=60,pady=120,anchor='sw')
    f2.pack(side='left',padx=60,anchor='n')

    Label(f1,text="Let's Get You Started.!",font=('arial_black 25 bold'),width=26,height=1,anchor='w',padx=5).pack()


    Label(f2,text="Email",font=('berlin_sans_fb 18 bold'),width=35,height=1,anchor='w',padx=5,bg='grey71').pack(padx=2,pady=5)
    em = StringVar()
    ema = Entry(f2, textvariable=em,font=(' 18 '),bg='grey71')
    ema.pack(fill=X,padx=10,pady=2)


    Label(f2,text="Password",font=('berlin_sans_fb 18 bold'),anchor='w',padx=5,bg='grey71').pack(side='top',pady=5,padx=2,anchor='w')

    ps = StringVar()
    psw = Entry(f2, textvariable=ps, font=(' 18 '),bg='grey71')
    psw.pack(fill=X,pady=5,side='top',anchor='se',padx=10)

    f3 = Frame(self, bg='grey71', relief=SUNKEN, borderwidth=2)
    f3.pack(side='left', padx=60, anchor='nw')

    f = IntVar()
    l = Checkbutton(f2,text="Lables", variable=f,bg='grey71',font=('berlin_sans_fb 15 bold'))
    l.pack(side=TOP,pady=15,padx=5,anchor='w')
    Label(f2,text='Description',font=(' 1 '),bg='grey71').pack(side=TOP,anchor='w',padx=30)

    def submit():
     try:
        print('emailid=', ema.get(), '\npassword=', psw.get())
        # giving info s to database
        i = c.connect(host='localhost', username='root', passwd=n, database='info')
        if i.is_connected():
            print('succesful')
            cur = i.cursor()
            h = "insert into information values('{}','{}')".format(str(ema.get()), str(psw.get()))
            print(h)
            cur.execute(h)
            i.commit()
            if f.get()==1:
                a = tmsg.showinfo('Massege.',
                          f"emailid:{ema.get()} \'n Password:{psw.get}\'n is succesfully registered")
     except:
         print('Try other password!')
         a = tmsg.showinfo('WARNING!',
                   "Try Another password")

    Button(f2,relief=SUNKEN,text="Register",font=('bell_mt 13 bold'),fg='thistle1',bg='gray2',borderwidth=5,height=0,command=submit,overrelief=RAISED,).pack(side=TOP,fill=X,padx=40,pady=10)



    self.mainloop()


def nn():
    root = Tk()
    root.geometry()
    Label(root, text='mysql passwd').pack()
    pas = StringVar
    pasw = Entry(root, textvariable=pas, font=(' 18 '), bg='grey71')
    pasw.pack(fill=X)
    Button(root, text='ENTER').pack()
    root.mainloop()


por()
