import calendar
import datetime
from tkinter import *
import random
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
        l33 = Label(f3, text='Contact No', font=("Calibiri", 13))
        l34 = Label(f3, text='CheckIn Date', font=("Calibiri", 13))
        l35 = Label(f3, text='CheckOut Date', font=("Calibiri", 13))
        l36 = Label(f3, text='Aadhar No', font=("Calibiri", 13))
        l31.place(x=150, y=20)
        l32.place(x=75, y=140)
        l33.place(x=75, y=180)
        l34.place(x=75, y=220)
        l35.place(x=75, y=260)
        l36.place(x=75, y=300)
        e11 = Entry(f3)
        e12 = Entry(f3)
        e13 = Entry(f3)
        e14 = Entry(f3)
        e15 = Entry(f3)
        b21 = Button(f3, text='Book')
        b22 = Button(f3, text='Cancel')
        b21.place(x=100, y=600)
        b22.place(x=200, y=600)
        l37 = Label(f3, text='Destination', font=("Calibiri", 13))
        l38 = Label(f3, text='Hotel', font=("Calibiri", 13))
        l39 = Label(f3, text='Room Type', font=("Calibiri", 13))
        #l310 = Label(f3, text=s1, font=("Calibiri", 13))
        #l311 = Label(f3, text=s2, font=("Calibiri", 13))
        #l312 = Label(f3, text=s3, font=("Calibiri", 13))
        l37.place(x=75, y=400)
        l38.place(x=75, y=440)
        l39.place(x=75, y=480)
        #l310.place(x=250, y=400)
        #l311.place(x=250, y=440)
        #l312.place(x=250, y=480)

        def on_click1(event):
            # global fclick
            fclick = True
            if fclick:
                fclick = False
                e13.delete(0, 'end')

        e13.insert(0, 'YYYY / MM / DD')
        e13.bind('<FocusIn>', on_click1)

        def on_click(event):
            # global firstclick
            firstclick = True
            if firstclick:
                firstclick = False
                e14.delete(0, 'end')

        e14.insert(0, 'YYYY / MM / DD')
        e14.bind('<FocusIn>', on_click)
        def out(self):
            a=e13.get()
            j=a.split('/')
            #for i in j:
            b=j[0]
            c=j[1]
            f=j[2]
            m1=datetime.date(int(b),int(c),int(f))
            a1 = e14.get()
            h=a1.split('/')
            #for k in h:
            b1 = h[0]
            c1 = h[1]
            f1 = h[2]
            m2 = datetime.date(int(b1), int(c1), int(f1))
            m=m2-m1
            print(m)
            p=m.days
            n=p
            q=int(n)*1000
            print(q)

        e14.bind('<FocusOut>', out)
        e11.place(x=250, y=145)
        e12.place(x=250, y=185)
        e13.place(x=250, y=225)
        e14.place(x=250, y=265)
        e15.place(x=250, y=305)
        l313 = Label(f3, text="LoginID", font=("Calibiri", 13))
        l315 = Label(f3, text=str(r), font=("Calibiri", 13))
        l314 = Label(f3, text="Your Selections:", font=("Calibiri", 15))
        l313.place(x=75, y=100)
        l314.place(x=250, y=350)
        l315.place(x=250, y=100)
        f3.pack()
        d2.mainloop()


a=Info()
a.info_win()
