from tkinter import *
from tkinter import messagebox

def open_registration_form():
    n = Tk()
    n.geometry("1000x1000")
    Label(n, text="REGISTRATION FORM", fg="brown", font=("calibri", 20)).place(x=400,y=100)

    Label(n, text="FIRSTNAME", font=("aerial", 10)).place(x=300,y=200)
    Label(n, text="LASTNAME", font=("aerial", 10)).place(x=300,y=230)
    Label(n, text="EMAIL", font=("aerial", 10)).place(x=300,y=260)
    Label(n, text="PHONE NUMBER", font=("aerial", 10)).place(x=300,y=290)
    Label(n, text="ADDRESS", font=("aerial", 10)).place(x=300,y=320)
    Label(n, text="PAN CARD NUMBER", font=("aerial", 10)).place(x=300,y=350)
    Label(n, text="AADHAR NUMBER", font=("aerial", 10)).place(x=300,y=380)
    Label(n, text="NATIONALITY", font=("aerial", 10)).place(x=300,y=410)
    Label(n, text="GENDER", font=("aerial", 10)).place(x=300,y=440)
    Label(n, text="DATE OF BIRTH", font=("aerial", 10)).place(x=300,y=480)

    e1 = Entry(n)
    e1.place(x=500,y=200)
    f1 = Entry(n)
    f1.place(x=500,y=230)
    g1 = Entry(n)
    g1.place(x=500,y=260)
    h1 = Entry(n)
    h1.place(x=500,y=290)
    i1 = Entry(n)
    i1.place(x=500,y=320)
    j1 = Entry(n)
    j1.place(x=500,y=350)
    k1 = Entry(n)
    k1.place(x=500,y=380)
    l1 = Entry(n)
    l1.place(x=500,y=410)
    m1 = Entry(n)
    m1.place(x=500,y=480)

    Checkbutton(n, text="FEMALE").place(x=500,y=440)
    Checkbutton(n, text="MALE").place(x=580,y=440)

    def msgebox():
        messagebox.showinfo("abc company", "successfully registered")

    Button(n, text="Confirm", command=msgebox).place(x=450,y=600)

    n.mainloop()

m = Tk()
m.geometry("1000x1000")
m.title("abc company")

a = Label(m, text="SIGN UP", fg="purple", font=("calibri", 50))
a.place(x=400, y=100)

b = Label(m, text="USERNAME / EMAIL", fg="black", font=("roman", 20))
b.place(x=300, y=300)

c = Label(m, text="PASSWORD", fg="black", font=("roman", 20))
c.place(x=300, y=450)

b1 = Entry(m)
b1.place(x=300, y=360)

c1 = Entry(m)
c1.place(x=300, y=500)

d = Button(m, text="SIGNUP", bg="blue", fg="white", activebackground="#0A66C2", command=open_registration_form, font=("roman", 20))
d.place(x=450, y=600)

m.config(bg="white")

m.mainloop()
