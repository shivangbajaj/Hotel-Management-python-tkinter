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
                #dest.disp_win(self)
        b1.bind('<Button-1>',click)
        logwin.bind('<Return>', click)

        l1.pack()
        frame1.pack()
        logwin.mainloop()



class Ainfo():
    def Ainfo_win(self):
        d2=Tk()
        d2.title("Hotel Management System")
        d2.geometry("700x650+200+50")
        global r
        r = random.randint(300000, 399999)
        f3=Frame(d2,width=700,height=700)
        l31=Label(f3,justify='center',text='CUSTOMER DETAILS')
        l31.config(font=("Arial", 28))
        l32=Label(f3,text='Name',font=("Calibiri",13))
        l33 = Label(f3, text='Contact No',font=("Calibiri",13))
        l34 = Label(f3, text='Aadhar No',font=("Calibiri",13))
        l35 = Label(f3, text='CheckIn Date',font=("Calibiri",13))
        l36 = Label(f3, text='CheckOut Date',font=("Calibiri",13))
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
        b21=Button(f3,text='Book')
        b22=Button(f3,text='Cancel')
        b21.place(x=100,y=600)
        b22.place(x=200,y=600)
        l37 = Label(f3, text='Destination', font=("Calibiri", 13))
        l38 = Label(f3, text='Hotel', font=("Calibiri", 13))
        l39 = Label(f3, text='Room Type', font=("Calibiri", 13))
        l310 = Label(f3, text=s1, font=("Calibiri", 13))
        l311 = Label(f3, text=s2, font=("Calibiri", 13))
        l312 = Label(f3, text=s3, font=("Calibiri", 13))
        l37.place(x=75, y=400)
        l38.place(x=75, y=440)
        l39.place(x=75, y=480)
        l310.place(x=250, y=400)
        l311.place(x=250, y=440)
        l312.place(x=250, y=480)
        def on_click1(event):
            #global fclick
            fclick = True
            if fclick:
                fclick = False
                e14.delete(0, 'end')
        e14.insert(0, 'YYYY / MM / DD')
        e14.bind('<FocusIn>', on_click1)
        def on_click(event):
            #global firstclick
            firstclick = True
            if firstclick:
                firstclick=False
                e15.delete(0,'end')
        e15.insert(0,'YYYY / MM / DD')
        e15.bind('<FocusIn>',on_click)
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
        def insertrec(self):
            db=pymysql.connect(host='localhost',user='root',password='root',database='hotel')
            c=db.cursor()
            s4 = e11.get()
            s5 = e12.get()
            s6 = e13.get()
            s7 = e14.get()
            s8 = e15.get()

            try:
                strr="insert into datab values("+str(r)+",'"+s4+"','"+s1+"','"+s2+"','"+s3+"',"+s5+","+s6+",'"+s7+"','"+s8+"');"
                c.execute(strr)
                msg = messagebox.showinfo('Message', 'Insert Successful')
            except pymysql.err.ProgrammingError:
                msg = messagebox.showinfo('Error!', 'Enter Valid Data!')
            db.commit()
            c.close()
            db.close()
            d2.destroy()
            dest.disp_win(self)
        b21.bind('<Button-1>',insertrec)
        f3.pack()
        d2.mainloop()


euser = 'angrymangoman@gmail.com'
epw = '38'
subject = 'Confirmation'
msg = MIMEMultipart()
msg['From'] = euser
msg['To'] = esend
msg['Subject'] = subject
body = 'Hey!Thanks for using my app to book for your holidays!! \nYour details are as follows: \nUsername : ' + un + '\nLoginID : ' + str(
    r) + '\nName : ' + s4 + '\nDestination : ' + s1 + '\nHotel : ' + s2 + '\nRoom : ' + s3 + '\nContactNo : ' + s5 + '\nCheckIn Date : ' + s7 + '\nCheckOut Date : ' + s8 + '\nTotal Cost : ' + str(
    q) + '\nThank You!!!'
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
server = smtplib.SMTP('smtp.googlemail.com', 587)
server.starttls()
server.login(euser, epw)
server.sendmail(euser, esend, text)
server.quit()
