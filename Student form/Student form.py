from tkinter import*
from tkinter.ttk import *
from time import strftime
def savefile():
    userinfo=userentry.get()
    passwordinfo=passwordentry.get()
    ageinfo=ageentry.get()
    Classinfo=Classentry.get()
    file = open("form.txt","w")
    
    file.write("Applicant name: " + userinfo)
    
    file.write("\n")
    
    file.write("Applicatn password:   " + passwordinfo)
    
    file.write("\n")
    
    file.write("Applicant age: " +ageinfo)
    file.write("\n")
    
    file.write("Applicant class: " +Classinfo)
    
    file.close()
    root.quit()
root=Tk()
root.title("School Registration Form")
root.wm_iconbitmap('favicon.ico')
root.geometry("300x200")
root.minsize(300, 200)
root.maxsize(300, 200)
user=Label(text="Name",font="Helvetica 19")
password=Label(text="Password",font="Helvetica 19")
age=Label(text="Age",font="Helvetica 19")
Class=Label(text="Class",font="Helvetica 19")
user.grid()
password.grid()
age.grid()
Class.grid()
uservalue=StringVar()
passwordvalue=StringVar()
agevalue=StringVar()
Classvalue=StringVar()
userentry=Entry(root,textvariable=uservalue)
passwordentry=Entry(root,textvariable=passwordvalue)
ageentry=Entry(root,textvariable=agevalue)
Classentry=Entry(root,textvariable=Classvalue)
userentry.grid(row=0,column=1)
passwordentry.grid(row=1,column=1)
ageentry.grid(row=2,column=1)
Classentry.grid(row=3,column=1)
Btn=Button(text="Submit",command=savefile)
Btn.place(x=125,y=150)

root.mainloop()
