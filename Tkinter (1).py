from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import ttk, messagebox
root = Tk()

TABLE_NAME = "management_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"

connection = sqlite3.connect('student_database.db')
connection.execute("CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " (" + STUDENT_ID +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, " +
                   STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER);" )

appLabel = tk.Label(root, text="Student Details Form", fg="#000000", width=35, font=("Arial Black", 30))
appLabel.place(x=200, y=5)

class Student:
    studentName = ""
    collegeName = ""
    phoneNumber = 0
    address = ""

    def __init__(self, studentName, collegeName, phoneNumber, address):
        self.studentName = studentName
        self.collegeName = collegeName
        self.phoneNumber = phoneNumber
        self.address = address

nameLabel = tk.Label(root, text="Enter your name", width=40, anchor='w',
                     font=("Sylfaen", 12))
nameLabel.place(x=270, y=80)

collegeLabel = tk.Label(root, text="Enter your college", width=40, anchor='w',
                        font=("Sylfaen", 12))
collegeLabel.place(x=270, y=160)

phoneLabel = tk.Label(root, text="Enter your phone", width=40, anchor='w',
                      font=("Sylfaen", 12))
phoneLabel.place(x=270, y=240)

addressLabel = tk.Label(root, text="Enter your address", width=40, anchor='w',
                        font=("Sylfaen", 12))
addressLabel.place(x=270, y=320)

nameEntry = tk.Entry(root, width=30)
nameEntry.place(x=800, y=80)

collegeEntry = tk.Entry(root, width=30)
collegeEntry.place(x=800, y=160)

phoneEntry = tk.Entry(root, width=30)
phoneEntry.place(x=800, y=240)

addressEntry = tk.Entry(root, width=30)
addressEntry.place(x=800, y=320)

def takeNameInput():
    global nameEntry, collegeEntry, phoneEntry, addressEntry
    global TABLE_NAME, STUDENT_NAME, STUDENT_COLLEGE, STUDENT_ADDRESS, STUDENT_PHONE
    username = nameEntry.get()
    nameEntry.delete(0, tk.END)
    collegeName = collegeEntry.get()
    collegeEntry.delete(0, tk.END)
    phone = int(phoneEntry.get())
    phoneEntry.delete(0, tk.END)
    address = addressEntry.get()
    addressEntry.delete(0, tk.END)

    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " +
                       STUDENT_COLLEGE + ", " + STUDENT_ADDRESS + ", " +
                       STUDENT_PHONE + " ) VALUES ( '"
                       + username + "', '" + collegeName + "', '" +
                       address + "', " + str(phone) + " );")
    connection.commit()
    messagebox.showinfo("Success", "Data Saved Successfully.")

def destroyRootWindow():
    secondWindow = tk.Tk()
    secondWindow.title("Display results")
    appLabel = tk.Label(secondWindow, text="Student Management System", fg="#06a099", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()
    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("one", "two", "three", "four")
    tree.heading("one", text="Student Name")
    tree.heading("two", text="College Name")
    tree.heading("three", text="Address")
    tree.heading("four", text="Phone Number")
    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + ";")
    i = 0
    for row in cursor:
        tree.insert('', i, text="Student " + str(row[0]),
                    values=(row[1], row[2], row[3], row[4]))
        i = i + 1
    tree.pack()
    secondWindow.mainloop()

button = tk.Button(root, text="Take Input", command=takeNameInput)
button.place(x=500, y=400)

displayButton = tk.Button(root, text="Display result", command=destroyRootWindow)
displayButton.place(x=800, y=400)

root.mainloop()
