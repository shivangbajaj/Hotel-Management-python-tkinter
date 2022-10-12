from tkinter import *
import pymysql
from tkinter import messagebox
import random
import datetime
s1=""
s2=""
s3=""
file='user.txt'
q=0
fclick = True
firstclick = True
cs=0
import tkinter.scrolledtext as tks
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Gui1:
    def sign(self):
        logwin1 = Tk()
        logwin1.geometry("300x180+400+200")
        logwin1.title("Hotel Management System")
        frame = Frame(logwin1, width=300, height=180)
        l111=Label(frame,text='Full Name')
        l112=Label(frame,text='Username')
        l113 = Label(frame, text='Password')
        l114 = Label(frame, text='Confirm Password')
        l111.place(x=20,y=20)
        l112.place(x=20,y=50)
        l113.place(x=20,y=80)
        l114.place(x=20,y=110)
        e111=Entry(frame)
        e112 = Entry(frame)
        e113 = Entry(frame)
        e114 = Entry(frame)
        e111.place(x=150, y=20)
        e112.place(x=150, y=50)
        e113.place(x=150, y=80)
        e114.place(x=150, y=110)

        def click2(self):
            if(e113.get() == e114.get()):
                db=pymysql.connect(host='localhost',user='root',password='root',database='hotel')
                c=db.cursor()
                a1=e111.get()
                a2 = e112.get()
                a3 = e113.get()
                try:
                    strr = "insert into login values('" + a1 + "','" + a2 + "','" + a3 + "')"
                    c.execute(strr)
                    msg = messagebox.showinfo('Message', 'SignedUp Successfully')
                except pymysql.err.ProgrammingError:
                    msg = messagebox.showinfo('Error!', 'Enter Valid Data!')
                db.commit()
                c.close()
                db.close()
#                with open(file,'a') as f1:
#                    f1.write(str(e112.get()))
#                    f1.write(' : ')
#                    f1.write(e113.get())
#                    f1.write('\n')
#                    f1.close()
                logwin1.destroy()
            else :
                msg=messagebox.showinfo('Error!','Password does not match')
        b=Button(frame,text='Signup')
        b.place(x=75,y=140)
        b.bind('<Button-1>',click2)
        frame.pack()
        logwin1.mainloop()

class GUI2:
    def main1(self):
        logwin = Tk()
        logwin.geometry("1200x628+200+50")
        logwin.title("Hotel Management System")
        img1 = PhotoImage(file ="C:\img\h1.png")
        frame1=Frame(logwin,width=700, height=700)
        l1=Label(frame1,image=img1)
        l2=Label(frame1,text='ADMIN LOGIN',fg='white',bg='black')
        l2.config(font=("Arial",28))
        l3=Label(frame1,text='Username',fg='white',bg='black')
        l4 = Label(frame1, text='Password', fg='white', bg='black')
        e1=Entry(frame1)
        e2 = Entry(frame1,show="*")
        b1=Button(frame1,text='Submit')
        l3.config(font=("Arial", 12))
        l4.config(font=("Arial", 12))
        l3.place(x=100,y=415)
        b1.place(x=200, y=475)
        e1.place(x=200, y=417)
        e2.place(x=200, y=447)
        l4.place(x=100, y=445)
        l2.place(x=100,y=350)

        def click(self):
            if(e1.get() == 'admin' and e2.get() == 'admin'):
                logwin.destroy()
                Ainfo.Ainfo_win(self)
        b1.bind('<Button-1>',click)
        logwin.bind('<Return>', click)

        def bck():
            logwin.destroy()
            GUI.main(self)

        b98 = Button(frame1, text="Back", command=bck)
        b98.place(x=10, y=10)

        l1.pack()
        frame1.pack()
        logwin.mainloop()


class Ainfo():
    def Ainfo_win(self):
        d2=Tk()
        d2.title("Hotel Management System")
        d2.geometry("900x650+200+50")
        f1 = Frame(d2, width=700, height=700)
        l11 = Label(f1, text='ADMIN', justify='center')
        l11.config(font=("Arial", 28))
        l11.grid(row=5,column=5)
        #l11.place(x=300,y=20)
        def disp_rec():
            db = pymysql.connect(host='localhost', user='root', password='root', database='hotel')
            c = db.cursor()
            strr="select * from datab;"
            c.execute(strr)
            r=c.fetchall()
            for row in r:
                s.insert(END,row)
                s.insert(END,'\n')
            db.close()
        def disp_rec1():
            db = pymysql.connect(host='localhost', user='root', password='root', database='hotel')
            c = db.cursor()
            str1 = "Select * from datab where LoginID = " + e1.get() + ";"
            c.execute(str1)
            r=c.fetchall()
            for row in r:
                s.insert(END,row)
                s.insert(END,'\n')
            db.close()
        def disp_rec2():
            db = pymysql.connect(host='localhost', user='root', password='root', database='hotel')
            c = db.cursor()
            str2 = "Select * from datab where Destination = '" + e2.get() + "';"
            c.execute(str2)
            r=c.fetchall()
            for row in r:
                s.insert(END,row)
                s.insert(END,'\n')
            db.close()
        def disp_rec3():
            s.delete('1.0','end')
        b=Button(f1,text='DISPLAY',height=2,width=10,bd=5,activebackground="blue",activeforeground="yellow",command=disp_rec)
        b.grid(row=10,column=5,pady=30)
        l12=Label(f1,text="Display all records:",font=("Arial",20))
        l12.grid(row=10, column=5, pady=30,sticky='sw')
        l13 = Label(f1, text="Search by LoginID:", font=("Arial", 14))
        l14 = Label(f1, text="Search by Destination:", font=("Arial", 14))
        l13.grid(row=15, column=5, sticky='sw')
        l14.grid(row=20, column=5, pady=20, sticky='sw')
        global e1
        e1=Entry(f1)
        global e2
        e2=Entry(f1)
        e1.grid(row=15, column=5)
        e2.grid(row=20, column=5, pady=20)
        b1 = Button(f1,text="SEARCH",activebackground="blue",activeforeground="yellow",command=disp_rec1)
        b2 = Button(f1, text="SEARCH",  activebackground="blue", activeforeground="yellow",command=disp_rec2)
        b1.grid(row=15, column=5, sticky='e')
        b2.grid(row=20, column=5, pady=20,sticky='e')
        b3 = Button(f1, text="CLEAR", activebackground="blue", activeforeground="yellow", command=disp_rec3)
        b3.grid(row=80, column=5, pady=20)
        #b.place(x=350,y=100)
        sb=Scrollbar(f1)
        sb1 = Scrollbar(f1,orient=HORIZONTAL)
        s=Text(f1,width=90,height=16,wrap=NONE,yscrollcommand=sb.set,xscrollcommand=sb1.set)
        s.grid(row=50,column=5,sticky='nsew')
        sb.config(command=s.yview)
        sb1.config(command=s.xview)
        sb.grid(row=50,column=70,sticky='nsew')
        sb1.grid(row=70, column=5, sticky='nsew')
        def lo():
            d2.destroy()
            GUI2.main1(self)
        b99=Button(f1,text="Logout",command=lo)
        b99.grid(row=5,column=80)
        #sb.pack(side='right',fill='y')
        #s.pack(side="left")
        #s=tks.ScrolledText(f1,width=150,height=15)
        #s.place(x=10,y=150)
        f1.pack()
        d2.mainloop()

class GUI:
    def main(self):
        logwin = Tk()
        logwin.geometry("1200x628+200+50")
        logwin.title("Hotel Management System")
        img1 = PhotoImage(file ="C:\img\h1.png")
        frame1=Frame(logwin,width=700, height=700)
        l1=Label(frame1,image=img1)
        l2=Label(frame1,text='LOGIN',fg='white',bg='black')
        l2.config(font=("Arial",28))
        l3=Label(frame1,text='Username',fg='white',bg='black')
        l4 = Label(frame1, text='Password', fg='white', bg='black')
        global e1
        e1=Entry(frame1)
        e2 = Entry(frame1,show="*")
        b1=Button(frame1,text='Submit')
        b2 = Button(frame1, text='Signup')
        b3 = Button(frame1, text='Admin Login')
        l3.config(font=("Arial", 12))
        l4.config(font=("Arial", 12))
        l3.place(x=100,y=415)
        b1.place(x=150, y=485)
        b2.place(x=250, y=485)
        #b3.place(x=1105,y=590)
        b3.place(x=1105, y=15)
        e1.place(x=200, y=417)
        e2.place(x=200, y=447)
        l4.place(x=100, y=445)
        l2.place(x=100,y=350)
        def click(self):
            db=pymysql.connect(host='localhost',user='root',password='root',database='hotel')
            c=db.cursor()
            strr = "select * from login where Username='"+e1.get()+"' and password='"+e2.get()+"';"
            if (c.execute(strr)):
                global un
                un=e1.get()
                logwin.destroy()
                dest.disp_win(self)
            else:
                msg = messagebox.showinfo('Error!', 'Wrong Username or password!')
            db.commit()
            c.close()
            db.close()
#            with open(file) as f:
#                data=f.read()
#                f.close()
#                if ((e1.get()+' : '+e2.get()) in data):
#                    logwin.destroy()
#                else:
#                    print ('erreo2')
        def click1(self):
            Gui1.sign(self)
        def click2(self):
            logwin.destroy()
            GUI2.main1(self)
        b1.bind('<Button-1>',click)
        b3.bind('<Button-1>', click2)
        logwin.bind('<Return>', click)
        b2.bind('<Button-1>', click1)
        l1.pack()
        frame1.pack()
        logwin.mainloop()

class Can():
    def cancel(self):
        d2 = Tk()
        d2.title("Hotel Management System")
        d2.geometry("900x650+200+50")
        f1 = Frame(d2, width=700, height=700)
        l11 = Label(f1, text='CANCEL BOOKING', justify='center')
        l11.config(font=("Arial", 28))
        l11.grid(row=5, column=5)

        def bck():
            d2.destroy()
            dest.disp_win(self)

        b98 = Button(f1, text="Back", command=bck)
        b98.grid(row=5, column=1)

        # l11.place(x=300,y=20)
        def disp_rec():
            db = pymysql.connect(host='localhost', user='root', password='root', database='hotel')
            c = db.cursor()
            strr = "select * from datab where Username='"+un+"';"
            c.execute(strr)
            r = c.fetchall()
            for row in r:
                s.insert(END, row)
                s.insert(END, '\n')
            db.close()

        def disp_rec1():
            db = pymysql.connect(host='localhost', user='root', password='root', database='hotel')
            c = db.cursor()
            try:
                str1 = "delete from datab where LoginID = " + e1.get() + ";"
                c.execute(str1)
                msg=messagebox.showinfo('Success','Deleted Successfully')
                db.commit()
            except:
                msg=messagebox.showinfo('Error!','Delete Unsuccessful')
            c.close()
            db.close()


        def disp_rec3():
            s.delete('1.0', 'end')

        b = Button(f1, text='DISPLAY', height=2, width=10, bd=5, activebackground="blue", activeforeground="yellow",
                   command=disp_rec)
        b.grid(row=10, column=5, pady=30)
        l12 = Label(f1, text="Display all your records:", font=("Arial", 16))
        l12.grid(row=10, column=5, pady=30, sticky='sw')
        l13 = Label(f1, text="Delete by LoginID:", font=("Arial", 14))
        l13.grid(row=15, column=5,pady=20, sticky='sw')
        global e1
        e1 = Entry(f1)
        e1.grid(row=15, column=5)
        b1 = Button(f1, text="DELETE", activebackground="blue", activeforeground="yellow", command=disp_rec1)
        b1.grid(row=15, column=5, sticky='e')
        b3 = Button(f1, text="CLEAR", activebackground="blue", activeforeground="yellow", command=disp_rec3)
        b3.grid(row=80, column=5, pady=20)
        # b.place(x=350,y=100)
        sb = Scrollbar(f1)
        sb1 = Scrollbar(f1, orient=HORIZONTAL)
        s = Text(f1, width=75, height=16, wrap=NONE, yscrollcommand=sb.set, xscrollcommand=sb1.set)
        s.grid(row=50, column=5, sticky='nsew')
        sb.config(command=s.yview)
        sb1.config(command=s.xview)
        sb.grid(row=50, column=70, sticky='nsew')
        sb1.grid(row=70, column=5, sticky='nsew')

        def lo():
            d2.destroy()
            GUI.main(self)

        b99 = Button(f1, text="Logout", command=lo)
        b99.grid(row=5, column=80)
        # sb.pack(side='right',fill='y')
        # s.pack(side="left")
        # s=tks.ScrolledText(f1,width=150,height=15)
        # s.place(x=10,y=150)
        f1.pack()
        d2.mainloop()


class dest():
    def disp_win(self):

        d=Tk()
        d.title("Hotel Management System")
        d.geometry("900x500+200+50")
        f1=Frame(d,width=700,height=700)
        i7 = PhotoImage(file="C:\img\w1.png")
        l12 = Label(f1, image=i7)
        l11=Label(f1,text='SELECT DESTINATION',justify='center')
        l11.config(font=("Arial", 32))
        def click9l(self):
            d.destroy()
            Can.cancel(self)
        b88 = Button(f1, text="Cancel Booking")
        b88.place(x=10, y=10)
        b88.bind('<Button-1>',click9l)
        i1 = PhotoImage(file="C:\img\Goa.png")
        i2 = PhotoImage(file="C:\img\leh10.png")
        i3 = PhotoImage(file="C:\img\Agra1.png")
        i4 = PhotoImage(file="C:\img\manali.png")
        i5 = PhotoImage(file="C:\img\ooty.png")
        i6 = PhotoImage(file="C:\img\mumbai.png")
        b1 = Button(f1,image=i1,height=133,width=200,borderwidth=0)
        b2 = Button(f1, image=i3,height=133,width=200,  borderwidth=0)
        b3 = Button(f1, image=i2,height=133,width=200,  borderwidth=0)
        b4 = Button(f1, image=i4,height=133,width=200, borderwidth=0)
        b5 = Button(f1, image=i5,height=133,width=200, borderwidth=0)
        b6 = Button(f1, image=i6,height=133,width=200, borderwidth=0)
        b1.place(x=100,y=120)
        b2.place(x=350, y=120)
        b3.place(x=600, y=120)
        b4.place(x=100, y=300)
        b5.place(x=350, y=300)
        b6.place(x=600, y=300)
        l11.place(x=225,y=25)
        def click11(self):
            global s1
            s1 = "Goa"
            d.destroy()
            hotel.hotel_win(self)
        def click12(self):
            global s1
            s1 = "Agra"
            d.destroy()
            hotel.hotel_win(self)
        def click13(self):
            global s1
            s1 = "Leh"
            d.destroy()
            hotel.hotel_win(self)
        def click14(self):
            global s1
            s1 = "Manali"
            d.destroy()
            hotel.hotel_win(self)
        def click15(self):
            global s1
            s1 = "Ooty"
            d.destroy()
            hotel.hotel_win(self)
        def click16(self):
            global s1
            s1 = "Mumbai"
            d.destroy()
            hotel.hotel_win(self)
        b1.bind('<Button-1>', click11)
        b2.bind('<Button-1>', click12)
        b3.bind('<Button-1>', click13)
        b4.bind('<Button-1>', click14)
        b5.bind('<Button-1>', click15)
        b6.bind('<Button-1>', click16)
        def lo():
            d.destroy()
            GUI.main(self)
        b99=Button(f1,text="Logout",command=lo)
        b99.place(x=825,y=10)
        l12.pack()
        f1.pack()
        d.mainloop()

class hotel():
    def hotel_win(self):
        d1=Tk()
        d1.title("Hotel Management System")
        d1.geometry("900x500+200+50")
        f2=Frame(d1,width=700,height=700)
        i7 = PhotoImage(file="C:\img\w1.png")
        l12 = Label(f2, image=i7)
        i21 = PhotoImage(file="C:\img\ho11.png")
        i22 = PhotoImage(file="C:\img\ho22.png")
        i23 = PhotoImage(file="C:\img\ho33.png")
        i24 = PhotoImage(file="C:\img\ho44.png")
        i25 = PhotoImage(file="C:\img\ho55.png")
        i26 = PhotoImage(file="C:\img\ho66.png")
        if(s1 == 'Goa'):
            l31 = Label(f2, text="Colva Kinara")
            l32 = Label(f2, text="Sapphire Comfort")
            l33 = Label(f2, text="Amigo Plaza")
            l34 = Label(f2, text="Hotel La Grace")
            l35 = Label(f2, text="Sincro Hotel")
            l36 = Label(f2, text="Farmagudi Residency")
            b11 = Button(f2,image=i21,height=110,width=175,borderwidth=0)
            b12 = Button(f2, image=i22,height=110,width=175,borderwidth=0)
            b13 = Button(f2, image=i23,height=110,width=175,borderwidth=0)
            b14 = Button(f2, image=i24,height=110,width=175,borderwidth=0)
            b15 = Button(f2, image=i25,height=110,width=175,borderwidth=0)
            b16 = Button(f2, image=i26,height=110,width=175,borderwidth=0)
            b11.place(x=100,y=110)
            b12.place(x=350, y=110)
            b13.place(x=600, y=110)
            b14.place(x=100, y=300)
            b15.place(x=350, y=300)
            b16.place(x=600, y=300)
            l21 = Label(f2, text='SELECT HOTEL:GOA', justify='center')
            l21.config(font=("Arial", 32))
            l21.place(x=260,y=25)
            def click21(self):
                global s2
                s2 = "Colva Kinara"
                d1.destroy()
                room.room_win(self)
            def click22(self):
                global s2
                s2 = "Sapphire Comfort"
                d1.destroy()
                room.room_win(self)
            def click23(self):
                global s2
                s2 = "Amigo Plaza"
                d1.destroy()
                room.room_win(self)
            def click24(self):
                global s2
                s2 = "Hotel La Grace"
                d1.destroy()
                room.room_win(self)
            def click25(self):
                global s2
                s2 = "Sincro Hotel"
                d1.destroy()
                room.room_win(self)
            def click26(self):
                global s2
                s2 = "Farmagudi Residency"
                d1.destroy()
                room.room_win(self)
            b11.bind('<Button-1>', click21)
            b12.bind('<Button-1>', click22)
            b13.bind('<Button-1>', click23)
            b14.bind('<Button-1>', click24)
            b15.bind('<Button-1>', click25)
            b16.bind('<Button-1>', click26)
        if (s1 == 'Agra'):
            l31 = Label(f2, text="Atulyaa Taj")
            l32 = Label(f2, text="Hotel Four Points")
            l33 = Label(f2, text="Taj Inn")
            l34 = Label(f2, text="Royal Residency")
            l35 = Label(f2, text="Seven Hills Hotel")
            l36 = Label(f2, text="Hilton Hotel")
            b11 = Button(f2, image=i23,height=110,width=175,borderwidth=0)
            b12 = Button(f2, image=i24,height=110,width=175,borderwidth=0)
            b13 = Button(f2, image=i26,height=110,width=175,borderwidth=0)
            b14 = Button(f2, image=i21,height=110,width=175,borderwidth=0)
            b15 = Button(f2, image=i25,height=110,width=175,borderwidth=0)
            b16 = Button(f2, image=i22,height=110,width=175,borderwidth=0)
            b11.place(x=100, y=120)
            b12.place(x=350, y=120)
            b13.place(x=600, y=120)
            b14.place(x=100, y=300)
            b15.place(x=350, y=300)
            b16.place(x=600, y=300)
            l21 = Label(f2, text='SELECT HOTEL:AGRA', justify='center')
            l21.config(font=("Arial", 32))
            l21.place(x=260, y=25)

            def click21(self):
                global s2
                s2 = "Atulyaa Taj"
                d1.destroy()
                room.room_win(self)

            def click22(self):
                global s2
                s2 = "Hotel Four Points"
                d1.destroy()
                room.room_win(self)

            def click23(self):
                global s2
                s2 = "Taj Inn"
                d1.destroy()
                room.room_win(self)

            def click24(self):
                global s2
                s2 = "Royal Residency"
                d1.destroy()
                room.room_win(self)

            def click25(self):
                global s2
                s2 = "Seven Hills Hotel"
                d1.destroy()
                room.room_win(self)

            def click26(self):
                global s2
                s2 = "Hilton Hotel"
                d1.destroy()
                room.room_win(self)

            b11.bind('<Button-1>', click21)
            b12.bind('<Button-1>', click22)
            b13.bind('<Button-1>', click23)
            b14.bind('<Button-1>', click24)
            b15.bind('<Button-1>', click25)
            b16.bind('<Button-1>', click26)
        if (s1 == 'Leh'):
            l31 = Label(f2, text="Khardungla View")
            l32 = Label(f2, text="Reenam Hotel")
            l33 = Label(f2, text="Hotel Hill Town")
            l34 = Label(f2, text="Grand Dragon")
            l35 = Label(f2, text="Hotel Antelope")
            l36 = Label(f2, text="Sangto Villa")
            b11 = Button(f2, image=i25,height=110,width=175,borderwidth=0)
            b12 = Button(f2, image=i26,height=110,width=175,borderwidth=0)
            b13 = Button(f2, image=i22,height=110,width=175,borderwidth=0)
            b14 = Button(f2, image=i24,height=110,width=175,borderwidth=0)
            b15 = Button(f2, image=i21,height=110,width=175,borderwidth=0)
            b16 = Button(f2, image=i23,height=110,width=175,borderwidth=0)
            b11.place(x=100, y=120)
            b12.place(x=350, y=120)
            b13.place(x=600, y=120)
            b14.place(x=100, y=300)
            b15.place(x=350, y=300)
            b16.place(x=600, y=300)
            l21 = Label(f2, text='SELECT HOTEL:LEH', justify='center')
            l21.config(font=("Arial", 32))
            l21.place(x=260, y=25)

            def click21(self):
                global s2
                s2 = "Khardungla View"
                d1.destroy()
                room.room_win(self)

            def click22(self):
                global s2
                s2 = "Reenam Hotel"
                d1.destroy()
                room.room_win(self)

            def click23(self):
                global s2
                s2 = "Hotel Hill Town"
                d1.destroy()
                room.room_win(self)

            def click24(self):
                global s2
                s2 = "Grand Dragon"
                d1.destroy()
                room.room_win(self)

            def click25(self):
                global s2
                s2 = "Hotel Antelope"
                d1.destroy()
                room.room_win(self)

            def click26(self):
                global s2
                s2 = "Sangto Villa"
                d1.destroy()
                room.room_win(self)

            b11.bind('<Button-1>', click21)
            b12.bind('<Button-1>', click22)
            b13.bind('<Button-1>', click23)
            b14.bind('<Button-1>', click24)
            b15.bind('<Button-1>', click25)
            b16.bind('<Button-1>', click26)
        if (s1 == 'Manali'):
            l31 = Label(f2, text="Manali Inn")
            l32 = Label(f2, text="Orchard Greens")
            l33 = Label(f2, text="Hotel Himgiri")
            l34 = Label(f2, text="Hotel Jupiter")
            l35 = Label(f2, text="Piccadily")
            l36 = Label(f2, text="Hotel Vintage")
            b11 = Button(f2, image=i22,height=110,width=175,borderwidth=0)
            b12 = Button(f2, image=i23,height=110,width=175,borderwidth=0)
            b13 = Button(f2, image=i25,height=110,width=175,borderwidth=0)
            b14 = Button(f2, image=i26,height=110,width=175,borderwidth=0)
            b15 = Button(f2, image=i24,height=110,width=175,borderwidth=0)
            b16 = Button(f2, image=i21,height=110,width=175,borderwidth=0)
            b11.place(x=100, y=120)
            b12.place(x=350, y=120)
            b13.place(x=600, y=120)
            b14.place(x=100, y=300)
            b15.place(x=350, y=300)
            b16.place(x=600, y=300)
            l21 = Label(f2, text='SELECT HOTEL:MANALI', justify='center')
            l21.config(font=("Arial", 32))
            l21.place(x=260, y=25)

            def click21(self):
                global s2
                s2 = "Manali Inn"
                d1.destroy()
                room.room_win(self)

            def click22(self):
                global s2
                s2 = "Orchard Greens"
                d1.destroy()
                room.room_win(self)

            def click23(self):
                global s2
                s2 = "Hotel Himgiri"
                d1.destroy()
                room.room_win(self)

            def click24(self):
                global s2
                s2 = "Hotel Jupiter"
                d1.destroy()
                room.room_win(self)

            def click25(self):
                global s2
                s2 = "Piccadily"
                d1.destroy()
                room.room_win(self)

            def click26(self):
                global s2
                s2 = "Hotel Vintage"
                d1.destroy()
                room.room_win(self)

            b11.bind('<Button-1>', click21)
            b12.bind('<Button-1>', click22)
            b13.bind('<Button-1>', click23)
            b14.bind('<Button-1>', click24)
            b15.bind('<Button-1>', click25)
            b16.bind('<Button-1>', click26)
        if (s1 == 'Ooty'):
            l31 = Label(f2, text="Majestic Crown")
            l32 = Label(f2, text="Lake View")
            l33 = Label(f2, text="Heaven Hotel")
            l34 = Label(f2, text="Delight Inn")
            l35 = Label(f2, text="Silver Oak")
            l36 = Label(f2, text="Glenpark Inn")
            b11 = Button(f2, image=i24,height=110,width=175,borderwidth=0)
            b12 = Button(f2, image=i25,height=110,width=175,borderwidth=0)
            b13 = Button(f2, image=i21,height=110,width=175,borderwidth=0)
            b14 = Button(f2, image=i22,height=110,width=175,borderwidth=0)
            b15 = Button(f2, image=i26,height=110,width=175,borderwidth=0)
            b16 = Button(f2, image=i23,height=110,width=175,borderwidth=0)
            b11.place(x=100, y=120)
            b12.place(x=350, y=120)
            b13.place(x=600, y=120)
            b14.place(x=100, y=300)
            b15.place(x=350, y=300)
            b16.place(x=600, y=300)
            l21 = Label(f2, text='SELECT HOTEL:OOTY', justify='center')
            l21.config(font=("Arial", 32))
            l21.place(x=260, y=25)

            def click21(self):
                global s2
                s2 = "Majestic Crown"
                d1.destroy()
                room.room_win(self)

            def click22(self):
                global s2
                s2 = "Lake View"
                d1.destroy()
                room.room_win(self)

            def click23(self):
                global s2
                s2 = "Heaven Hotel"
                d1.destroy()
                room.room_win(self)

            def click24(self):
                global s2
                s2 = "Delight Inn"
                d1.destroy()
                room.room_win(self)

            def click25(self):
                global s2
                s2 = "Silver Oak"
                d1.destroy()
                room.room_win(self)

            def click26(self):
                global s2
                s2 = "Glenpark Inn"
                d1.destroy()
                room.room_win(self)

            b11.bind('<Button-1>', click21)
            b12.bind('<Button-1>', click22)
            b13.bind('<Button-1>', click23)
            b14.bind('<Button-1>', click24)
            b15.bind('<Button-1>', click25)
            b16.bind('<Button-1>', click26)
        if (s1 == 'Mumbai'):
            l31 = Label(f2, text="Taj Palace")
            l32 = Label(f2, text="Oberoi Hotel")
            l33 = Label(f2, text="Pristine Residency")
            l34 = Label(f2, text="Grand Hyatt")
            l35 = Label(f2, text="Kohinoor Hotel")
            l36 = Label(f2, text="JW Marriott")
            b11 = Button(f2, image=i26,height=110,width=175,borderwidth=0)
            b12 = Button(f2, image=i21,height=110,width=175,borderwidth=0)
            b13 = Button(f2, image=i23,height=110,width=175,borderwidth=0)
            b14 = Button(f2, image=i24,height=110,width=175,borderwidth=0)
            b15 = Button(f2, image=i22,height=110,width=175,borderwidth=0)
            b16 = Button(f2, image=i25,height=110,width=175,borderwidth=0)
            b11.place(x=100, y=120)
            b12.place(x=350, y=120)
            b13.place(x=600, y=120)
            b14.place(x=100, y=300)
            b15.place(x=350, y=300)
            b16.place(x=600, y=300)
            l21 = Label(f2, text='SELECT HOTEL:MUMBAI', justify='center')
            l21.config(font=("Arial", 32))
            l21.place(x=260, y=25)

            def click21(self):
                global s2
                s2 = "Taj Palace"
                d1.destroy()
                room.room_win(self)

            def click22(self):
                global s2
                s2 = "Oberoi Hotel"
                d1.destroy()
                room.room_win(self)

            def click23(self):
                global s2
                s2 = "Pristine Residency"
                d1.destroy()
                room.room_win(self)

            def click24(self):
                global s2
                s2 = "Grand Hyatt"
                d1.destroy()
                room.room_win(self)

            def click25(self):
                global s2
                s2 = "Kohinoor Hotel"
                d1.destroy()
                room.room_win(self)

            def click26(self):
                global s2
                s2 = "JW Marriott"
                d1.destroy()
                room.room_win(self)

            b11.bind('<Button-1>', click21)
            b12.bind('<Button-1>', click22)
            b13.bind('<Button-1>', click23)
            b14.bind('<Button-1>', click24)
            b15.bind('<Button-1>', click25)
            b16.bind('<Button-1>', click26)
        l31.config(font=("Arial",13),fg='blue')
        l31.place(x=105,y=232)
        l32.config(font=("Arial", 13),fg='blue')
        l32.place(x=355, y=232)
        l33.config(font=("Arial", 13),fg='blue')
        l33.place(x=605, y=232)
        l34.config(font=("Arial", 13),fg='blue')
        l34.place(x=105, y=412)
        l35.config(font=("Arial", 13),fg='blue')
        l35.place(x=355, y=412)
        l36.config(font=("Arial", 13),fg='blue')
        l36.place(x=605, y=412)

        def bck():
            d1.destroy()
            dest.disp_win(self)
        b98=Button(f2,text="Back",command=bck)
        b98.place(x=10,y=10)
        def lo():
            d1.destroy()
            GUI.main(self)
        b99=Button(f2,text="Logout",command=lo)
        b99.place(x=825,y=10)
        l12.pack()
        f2.pack()
        d1.mainloop()
class room():
    def room_win(self):

        d3=Tk()
        d3.title("Hotel Management System")
        d3.geometry("900x500+200+50")
        f4=Frame(d3,width=900,height=500)
        i7 = PhotoImage(file="C:\img\w1.png")
        l12 = Label(f4, image=i7)
        l12.pack()
        db = pymysql.connect(host='localhost', user='root', password='root', database='hotel')
        c = db.cursor()
        c.execute("select * from avail where hotel = '"+s1+"';")
        global r
        for r in c.fetchall():
            r1 = r[1]
            r2 = r[2]
            r3 = r[3]
            r4 = r[4]
            r5 = r[5]
            r6 = r[6]
        l41=Label(f4,text='SELECT ROOM',justify='center')
        l41.config(font=("Arial", 28))
        i21 = PhotoImage(file="C:\img\R1.png")
        i22 = PhotoImage(file="C:\img\R2.png")
        i23 = PhotoImage(file="C:\img\R3.png")
        i24 = PhotoImage(file="C:\img\R4.png")
        i25 = PhotoImage(file="C:\img\R5.png")
        i26 = PhotoImage(file="C:\img\R6.png")
        b31 = Button(f4,image=i21,height=110,width=175,borderwidth=0)
        b32 = Button(f4, image=i22,height=110,width=175,borderwidth=0)
        b33 = Button(f4, image=i23,height=110,width=175,borderwidth=0)
        b34 = Button(f4, image=i24,height=110,width=175,borderwidth=0)
        b35 = Button(f4, image=i25,height=110,width=175,borderwidth=0)
        b36 = Button(f4, image=i26,height=110,width=175,borderwidth=0)
        l31 = Label(f4, text="Standard(1000)")
        l32 = Label(f4, text="Duplex(1700)")
        l33 = Label(f4, text="Suite(1300)")
        l34 = Label(f4, text="Studio(1200)")
        l35 = Label(f4, text="King Sized(1600)")
        l36 = Label(f4, text="Cabana(2000)")
        l31.config(font=("Arial", 13), fg='blue')
        l31.place(x=105, y=232)
        l32.config(font=("Arial", 13), fg='blue')
        l32.place(x=355, y=232)
        l33.config(font=("Arial", 13), fg='blue')
        l33.place(x=605, y=232)
        l34.config(font=("Arial", 13), fg='blue')
        l34.place(x=105, y=412)
        l35.config(font=("Arial", 13), fg='blue')
        l35.place(x=355, y=412)
        l36.config(font=("Arial", 13), fg='blue')
        l36.place(x=605, y=412)
        b31.place(x=100, y=120)
        b32.place(x=350, y=120)
        b33.place(x=600, y=120)
        b34.place(x=100, y=300)
        b35.place(x=350, y=300)
        b36.place(x=600, y=300)
        t1 = str(r1) + " rooms available"
        l37 = Label(f4, text=t1)
        l37.config(font=("Arial", 13), fg='blue')
        l37.place(x=105, y=260)
        t2 = str(r2) + " rooms available"
        l38 = Label(f4, text=t2)
        l38.config(font=("Arial", 13), fg='blue')
        l38.place(x=355, y=260)
        t3 = str(r3) + " rooms available"
        l39 = Label(f4, text=t3)
        l39.config(font=("Arial", 13), fg='blue')
        l39.place(x=605, y=260)
        t4 = str(r4) + " rooms available"
        l310 = Label(f4, text=t4)
        l310.config(font=("Arial", 13), fg='blue')
        l310.place(x=105, y=440)
        t5 = str(r5) + " rooms available"
        l311 = Label(f4, text=t5)
        l311.config(font=("Arial", 13), fg='blue')
        l311.place(x=355, y=440)
        t6 = str(r6) + " rooms available"
        l312 = Label(f4, text=t6)
        l312.config(font=("Arial", 13), fg='blue')
        l312.place(x=605, y=440)
        l41.place(x=260,y=25)
        c.close()
        db.close()
        def click31(self):
            global cs
            global s3
            global ra
            global count
            count=r[1]
            ra="r1"
            s3 = "Standard"
            cs = 1000
            d3.destroy()
            Info.info_win(self)

        def click32(self):
            global s3
            global cs
            global ra
            global count
            count = r[2]
            ra = "r2"
            s3 = "Duplex"
            cs=1700
            d3.destroy()
            Info.info_win(self)

        def click33(self):
            global s3
            global cs
            global ra
            global count
            count = r[3]
            ra = "r3"
            s3 = "Suite"
            cs=1300
            d3.destroy()
            Info.info_win(self)

        def click34(self):
            global s3
            global cs
            global ra
            global count
            count = r[4]
            ra = "r4"
            s3 = "Studio"
            cs=1200
            d3.destroy()
            Info.info_win(self)

        def click35(self):
            global s3
            global cs
            global ra
            global count
            count = r[5]
            ra = "r5"
            s3 = "King Sized"
            cs=1600

            d3.destroy()
            Info.info_win(self)

        def click36(self):
            global s3
            global cs
            global ra
            global count
            count = r[6]
            ra = "r6"
            s3 = "Cabana"
            cs=2000
            d3.destroy()
            Info.info_win(self)

        b31.bind('<Button-1>', click31)
        b32.bind('<Button-1>', click32)
        b33.bind('<Button-1>', click33)
        b34.bind('<Button-1>', click34)
        b35.bind('<Button-1>', click35)
        b36.bind('<Button-1>', click36)
        def bck():
            d3.destroy()
            hotel.hotel_win(self)
        b98=Button(f4,text="Back",command=bck)
        b98.place(x=10,y=10)
        def lo():
            d3.destroy()
            GUI.main(self)
        b99=Button(f4,text="Logout",command=lo)
        b99.place(x=825,y=10)
        f4.pack()
        d3.mainloop()

class Info():
    def info_win(self):
        d2 = Tk()
        d2.title("Hotel Management System")
        d2.geometry("700x650+200+50")
        global r
        r = random.randint(300000, 399999)
        f3 = Frame(d2, width=700, height=700)
        l31 = Label(f3, justify='center', text='CUSTOMER DETAILS')
        l31.config(font=("Arial", 28))
        l32 = Label(f3, text='Name', font=("Calibiri", 13))
        l321 = Label(f3, text='Gender', font=("Calibiri", 13))
        l33 = Label(f3, text='Contact No', font=("Calibiri", 13))
        l34 = Label(f3, text='CheckIn Date', font=("Calibiri", 13))
        l35 = Label(f3, text='CheckOut Date', font=("Calibiri", 13))
        l36 = Label(f3, text='Email ID', font=("Calibiri", 13))
        l31.place(x=150, y=20)
        l32.place(x=75, y=135)
        l321.place(x=75, y=170)
        l33.place(x=75, y=205)
        l34.place(x=75, y=245)
        l35.place(x=75, y=285)
        l36.place(x=75, y=325)
        e11 = Entry(f3)
        e12 = Entry(f3)
        e13 = Entry(f3)
        e14 = Entry(f3)
        e15 = Entry(f3)
        b21 = Button(f3, text='Book')
        b22 = Button(f3, text='Cancel')
        b21.place(x=100, y=600)
        b22.place(x=200, y=600)
        def click(self):
            d2.destroy()
        b22.bind('<Button-1>',click)
        l37 = Label(f3, text='Destination', font=("Calibiri", 13))
        l38 = Label(f3, text='Hotel', font=("Calibiri", 13))
        l39 = Label(f3, text='Room Type', font=("Calibiri", 13))
        l310 = Label(f3, text=s1, font=("Calibiri", 13))
        l311 = Label(f3, text=s2, font=("Calibiri", 13))
        l312 = Label(f3, text=s3, font=("Calibiri", 13))
        l313 = Label(f3, text='Grand Total', font=("Calibiri", 15))

        def gender():
            global g
            if(var.get()==1):
                g="Male"
            if (var.get() == 2):
                g = "Female"
        var = IntVar()
        r1 = Radiobutton(f3, text="Male", value=1, variable=var,command=gender)
        r2 = Radiobutton(f3, text="Female", value=2, variable=var,command=gender)

        r1.place(x=250, y=175)
        r2.place(x=310, y=175)
        l37.place(x=75, y=420)
        l38.place(x=75, y=460)
        l39.place(x=75, y=500)
        l310.place(x=250, y=420)
        l311.place(x=250, y=460)
        l312.place(x=250, y=500)
        l313.place(x=125, y=540)

        def on_click1(event):
            global fclick
            if fclick:
                fclick = False
                e13.delete(0, 'end')

        e13.insert(0, 'YYYY / MM / DD')
        e13.bind('<FocusIn>', on_click1)

        def on_click(event):
            global firstclick
            if firstclick:
                firstclick = False
                e14.delete(0, 'end')

        e14.insert(0, 'YYYY / MM / DD')
        e14.bind('<FocusIn>', on_click)
        def out(self):

            a=e13.get()
            j=a.split('/')
            b=j[0]
            c=j[1]
            f=j[2]
            m1=datetime.date(int(b),int(c),int(f))
            a1 = e14.get()
            h=a1.split('/')
            b1 = h[0]
            c1 = h[1]
            f1 = h[2]
            m2 = datetime.date(int(b1), int(c1), int(f1))
            m=m2-m1
            p=m.days
            n=p
            global q
            q=int(n)*cs
            l314 = Label(f3, text=q, font=("Calibiri", 15))
            l314.place(x=300, y=540)


        e14.bind('<FocusOut>', out)
        e11.place(x=250, y=135)
        e12.place(x=250, y=205)
        e13.place(x=250, y=245)
        e14.place(x=250, y=285)
        e15.place(x=250, y=325)
        l314 = Label(f3, text=q, font=("Calibiri", 15))
        l314.place(x=300, y=540)
        l313 = Label(f3, text="LoginID", font=("Calibiri", 13))
        l315 = Label(f3, text=str(r), font=("Calibiri", 13))
        l314 = Label(f3, text="Your Selections:", font=("Calibiri", 15))
        l313.place(x=75, y=90)
        l314.place(x=250, y=375)
        l315.place(x=250, y=90)
        def insertrec(self):
            db=pymysql.connect(host='localhost',user='root',password='root',database='hotel')
            c=db.cursor()
            s4 = e11.get()
            if (s4==""):
                msg=messagebox.showinfo('Error!','Name field cannot be empty')
            s5 = e12.get()
            if (s5==""):
                msg=messagebox.showinfo('Error!','Contact field cannot be empty')
            esend = e15.get()
            if (esend==""):
                msg=messagebox.showinfo('Error!','Email field cannot be empty')
            s7 = e13.get()
            s8 = e14.get()
            if(s7=="YYYY/MM/DD" or s8=="YYYY/MM/DD"):
                msg=messagebox.showinfo('Error!','Date field cannot be empty')
            global g

            try:
                strr="insert into datab values('"+un+"',"+str(r)+",'"+s4+"','"+s1+"','"+s2+"','"+s3+"',"+s5+",'"+esend+"','"+s7+"','"+s8+"',"+str(q)+");"
                c.execute(strr)
                #db.commit()
                global count
                count=count-1
                #c.execute("update avail set '{}'='{}' where hotel='{}';".format(ra,str(count),s1))
                srt="update avail set "+ra+"="+str(count)+" where hotel='"+s1+"';"
                c.execute(srt)
                msg = messagebox.showinfo('Message', 'Booked Successfully,Check Your Mail')
                db.commit()

            except pymysql.err.ProgrammingError:
                msg = messagebox.showinfo('Error!', 'Enter Valid Data!')
            db.commit()
            db.commit()
            c.close()
            euser = 'unseentechnologies05@gmail.com'
            epw = 'unseen05'
            subject = 'Confirmation'
            msg = MIMEMultipart()
            msg['From'] = euser
            msg['To'] = esend
            msg['Subject'] = subject
            body = 'Hey!  Thanks for using my app to book for your holidays!!\n\n \nYour details are as follows:\n \nUsername : ' + un + '\nLoginID : ' + str(
                r) + '\nName : ' + s4 + '\nDestination : ' + s1 + '\nHotel : ' + s2 + '\nRoom : ' + s3 + '\nContactNo : ' + s5 + '\nCheckIn Date : ' + s7 + '\nCheckOut Date : ' + s8 + '\nTotal Cost : ' + str(
                q) + '\n\nThank You!!!'
            msg.attach(MIMEText(body, 'plain'))
            text = msg.as_string()
            server = smtplib.SMTP('smtp.googlemail.com', 587)
            server.starttls()
            server.login(euser, epw)
            server.sendmail(euser, esend, text)
            server.quit()

            d2.destroy()
            dest.disp_win(self)
        b21.bind('<Button-1>',insertrec)
        def bck():
            d2.destroy()
            room.room_win(self)
        b98=Button(f3,text="Back",command=bck)
        b98.place(x=10,y=10)
        f3.pack()
        d2.mainloop()


#a=Ainfo()
#a.Ainfo_win()
a=GUI()
a.main()
#a=dest()
#a.disp_win()
#standard
#duplex
#suite
#studio
#cabana
#king sized
