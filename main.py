import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

def funcregister():
    entry_firstname = entry1.get()
    entry_lastname = entry2.get()
    entry_email = entry3.get()
    with open("database.txt","a") as f :
        f.write(entry_firstname)
        f.write(",")
        f.write(entry_lastname)
        f.write(",")
        f.write(entry_email),f.write("\n")
    messagebox.showinfo("result","resister is sucsess")
    entry1.delete(0,ttk.END)
    entry2.delete(0,ttk.END)
    entry3.delete(0,ttk.END)
       

app = ttk.Window(themename="morph")
app.geometry('1000x500+500+250')
app.title("Registration form")
app.resizable(False,False)

label1=ttk.Label(text="HELLO WELCOME TO THIS PROGRAM",font=("impact",30,"bold"))
label1.grid(row=1,column=0,padx=150)

label2=ttk.Label(text="Please Enter your first name :",font=("arial",20,"bold"))
label2.grid(row=3,column=0,padx=150)

entry1=ttk.Entry(app,width=60)
entry1.grid(row=4,column=0,padx=150)

label3=ttk.Label(text="Please Enter your last name :",font=("arial",20,"bold"))
label3.grid(row=5,column=0,padx=150)

entry2=ttk.Entry(app,width=60)
entry2.grid(row=6,column=0,padx=150)

label4=ttk.Label(text="Please Enter your email :",font=("arial",20,"bold"))
label4.grid(row=7,column=0,padx=150)

entry3=ttk.Entry(app,width=60)
entry3.grid(row=8,column=0,padx=150)

button1=ttk.Button(app, text="SUBMIT" , width= 15 , style=SUCCESS,command=funcregister)
button1.grid(row=12,column=0,padx=150)

button2=ttk.Button(app, text="Quit" , width= 15 , style=DANGER ,command=quit)
button2.grid(row=15,column=0,padx=150)

app.mainloop()