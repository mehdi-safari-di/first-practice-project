import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

def check_line(entryname,entrypass):
    with open("database.txt","r") as file2:
        data = file2.readlines()
    for line in data:
        names = line.strip().split(",")
        if names[0] == entryname and names[3] == entrypass:
            return True   
    return False  

def check():
    listname = []
    listpass = []
    entryname = var1.get()
    entrypass = var2.get()
    with open("database.txt","r") as readfile:
        file1 = readfile.read().split()
    for i in file1 :
        j = (i.split(",")[0])
        listname.append(j)
    for i in file1 :
        u = (i.split(",")[3])
        listpass.append(u)    
    if entryname in listname and entrypass in listpass:
        messagebox.showinfo("result","Please Wait... ")
    if check_line(entryname,entrypass) :
            entryname = var1.get()
            entrypass = var2.get()
            messagebox.showinfo("result","Your login is successful")
            var1.delete(0,ttk.END)
            var2.delete(0,ttk.END)    
    else:
        messagebox.showwarning("result","Your information does not exist")

def newpage():
    app.destroy()
    app1 = ttk.Window(themename="litera")
    app1.geometry('900x400+500+250')
    app1.title("Enter form")
    app1.resizable(False,False)
    
    label0_p3=ttk.Label(app1,text="YOU CAN ENTER TO PROGRAM",font=("impact",30,"bold"))
    label0_p3.grid(row=0,column=0,padx=180,pady=50)

    label1_p3=ttk.Label(app1,text="Please Enter your name :",font=("arial",15,"bold"))
    label1_p3.grid(row=1,column=0, sticky = "W",padx=30)

    entry1_p3=ttk.Entry(app1,width=30)
    entry1_p3.grid(row=1,column=0,padx=280,pady=10,sticky=E)
    global var1
    var1 = entry1_p3  

    label2_p3=ttk.Label(app1,text="Please Enter your password :",font=("arial",15,"bold"))
    label2_p3.grid(row=2,column=0, sticky = "W",padx=30)

    entry2_p3=ttk.Entry(app1,width=30)
    entry2_p3.grid(row=2,column=0,padx=280,pady=10,sticky=E)
    global var2
    var2 = entry2_p3  

    button1_p3=ttk.Button(app1, text="ENTER" , width= 15 , command=check)
    button1_p3.grid(row=4,column=0,padx=200,pady=70,sticky=E)
    
    button2_p3=ttk.Button(app1, text="Quit" , width= 15 ,command=quit)
    button2_p3.grid(row=4,column=0,padx=200,pady=70,sticky=W)

    app1.mainloop()


def funcregister():
    entry_password = entry1_p2.get()
    entry_confpassword = entry2_p2.get()
    if str(entry_password) == str(entry_confpassword) and len(str(entry_password)) > 8 and len(str(entry_confpassword)) > 8 :
        entry_firstname = entry1.get()
        entry_lastname = entry2.get()
        entry_email = entry3.get()
        with open("database.txt","a") as f :
            f.write(entry_firstname)
            f.write(",")
            f.write(entry_lastname)
            f.write(",")
            f.write(entry_email)
            f.write(",")
            f.write(entry_password),f.write("\n")
        messagebox.showinfo("result","resister is sucsess")
        entry1.delete(0,ttk.END)
        entry2.delete(0,ttk.END)
        entry3.delete(0,ttk.END)
        entry1_p2.delete(0,ttk.END)
        entry2_p2.delete(0,ttk.END)
        newpage()
    else:
        messagebox.showwarning("result","Your password must be more than 8 characters long, and both passwords must match")

def nextpage():
    label0.grid_forget()
    label1.grid_forget()
    label2.grid_forget()
    label3.grid_forget()
    entry1.grid_forget()
    entry2.grid_forget()
    entry3.grid_forget()
    button1.grid_forget()
    button2.grid_forget()
    
    label0_p2.grid(row=0,column=0,padx=260,pady=50)
    label1_p2.grid(row=1,column=0, sticky = "W",padx=30)
    entry1_p2.grid(row=1,column=0,padx=280,pady=10,sticky=E)
    label2_p2.grid(row=2,column=0, sticky = "W",padx=30)
    entry2_p2.grid(row=2,column=0,padx=280,pady=10,sticky=E)
    button1_p2.grid(row=4,column=0,padx=200,pady=70,sticky=E)
    button2_p2.grid(row=4,column=0,padx=200,pady=70,sticky=W)

def previouspage():
    label0_p2.grid_forget()
    label1_p2.grid_forget()
    entry1_p2.grid_forget()
    label2_p2.grid_forget()
    entry2_p2.grid_forget()
    button1_p2.grid_forget()
    button2_p2.grid_forget()
    entry1_p2.delete(0,ttk.END)
    entry2_p2.delete(0,ttk.END)
    
    label0.grid(row=0,column=0,padx=260,pady=50)       
    label1.grid(row=1,column=0, sticky = "W",padx=30)
    entry1.grid(row=1,column=0,padx=280,pady=10,sticky=E)
    entry1.delete(0,ttk.END)
    label2.grid(row=2,column=0, sticky = "W",padx=30)
    entry2.grid(row=2,column=0,padx=280,pady=10,sticky=E)
    entry2.delete(0,ttk.END)
    label3.grid(row=3,column=0, sticky = "W",padx=30)
    entry3.grid(row=3,column=0,padx=280,pady=10,sticky=E)
    entry3.delete(0,ttk.END)
    button1.grid(row=4,column=0,padx=200,pady=70,sticky=E)
    button2.grid(row=4,column=0,padx=200,pady=70,sticky=W)   

#page1
app = ttk.Window(themename="litera")
app.geometry('1000x500+500+250')
app.title("Registration form")
app.resizable(False,False)

label0=ttk.Label(text="Register your details",font=("impact",30,"bold"))
label0.grid(row=0,column=0,padx=260,pady=50)

label1=ttk.Label(text="Please Enter your first name :",font=("arial",15,"bold"))
label1.grid(row=1,column=0, sticky = "W",padx=30)

entry1=ttk.Entry(app,width=30)
entry1.grid(row=1,column=0,padx=280,pady=10,sticky=E)

label2=ttk.Label(text="Please Enter your last name :",font=("arial",15,"bold"))
label2.grid(row=2,column=0, sticky = "W",padx=30)

entry2=ttk.Entry(app,width=30)
entry2.grid(row=2,column=0,padx=280,pady=10,sticky=E)

label3=ttk.Label(text="Please Enter your email :",font=("arial",15,"bold"))
label3.grid(row=3,column=0, sticky = "W",padx=30)

entry3=ttk.Entry(app,width=40)
entry3.grid(row=3,column=0,padx=280,pady=10,sticky=E)

button1=ttk.Button(app, text="NEXT" , width= 15 , style=INFO,command=nextpage)
button1.grid(row=4,column=0,padx=200,pady=70,sticky=E)

button2=ttk.Button(app, text="Quit" , width= 15 , style=DANGER ,command=quit)
button2.grid(row=4,column=0,padx=200,pady=70,sticky=W)



#page2
label0_p2=ttk.Label(text="Register your password",font=("impact",30,"bold"))
label0_p2.grid(row=0,column=0,padx=260,pady=50)
label0_p2.grid_forget()

label1_p2=ttk.Label(text="Please Enter your Password :",font=("arial",15,"bold"))
label1_p2.grid(row=1,column=0, sticky = "W",padx=30)
label1_p2.grid_forget()

entry1_p2=ttk.Entry(app,width=30)
entry1_p2.grid(row=1,column=0,padx=280,pady=10,sticky=E)
entry1_p2.grid_forget()

label2_p2=ttk.Label(text="Please Enter your Confirm password :",font=("arial",15,"bold"))
label2_p2.grid(row=2,column=0, sticky = "W",padx=30)
label2_p2.grid_forget()

entry2_p2=ttk.Entry(app,width=30)
entry2_p2.grid(row=2,column=0,padx=280,pady=10,sticky=E)
entry2_p2.grid_forget()

button1_p2=ttk.Button(app, text="SUBMIT" , width= 15 , style=SUCCESS , command=funcregister)
button1_p2.grid(row=4,column=0,padx=200,pady=70,sticky=E)
button1_p2.grid_forget()

button2_p2=ttk.Button(app, text="BACK" , width= 15 , style=BASELINE , command=previouspage)
button2_p2.grid(row=4,column=0,padx=200,pady=70,sticky=W)
button2_p2.grid_forget()

app.mainloop()