from tkinter import *
file='user.txt'


class Gui1:
    def sign(self):
        logwin1 = Tk()
        logwin1.geometry("300x180+400+200")
        logwin1.title("Hotel Management System")
        frame = Frame(logwin1, width=300, height=180)
        l111=Label(frame,text='Name')
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
                with open(file,'a') as f1:
                    f1.write(str(e112.get()))
                    f1.write(' : ')
                    f1.write(e113.get())
                    f1.write('\n')
                    f1.close()
                    logwin1.destroy()
                    #GUI.main(self)
            else :
                print('Error')
        def lo():
            logwin1.destroy()
            GUI.main(self)
        b99=Button(frame,text="Logout",command=lo)
        b99.place(x=250,y=10)
        b=Button(frame,text='Signup')
        b.place(x=75,y=140)
        b.bind('<Button-1>',click2)
        frame.pack()
        logwin1.mainloop()


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
        e1=Entry(frame1)
        e2 = Entry(frame1,show="*")
        b1=Button(frame1,text='Submit')
        b2 = Button(frame1, text='Signup')
        l3.config(font=("Arial", 12))
        l4.config(font=("Arial", 12))
        l3.place(x=100,y=415)
        b1.place(x=200, y=475)
        b2.place(x=200, y=545)
        e1.place(x=200, y=417)
        e2.place(x=200, y=447)
        l4.place(x=100, y=445)
        l2.place(x=100,y=350)

        def click(self):
            with open(file) as f:
                data=f.read()
                f.close()
                if ((e1.get()+' : '+e2.get()) in data):
                    logwin.destroy()
                    Gui1.sign(self)
                else:
                    print ('erreo2')
                #dest.disp_win(self)
        def click1(self):
            #logwin.destroy()
            Gui1.sign(self)
        b1.bind('<Button-1>',click)
        logwin.bind('<Return>', click)
        b2.bind('<Button-1>', click1)
        l1.pack()
        frame1.pack()
        logwin.mainloop()


a = GUI()
a.main()
