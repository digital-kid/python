from tkinter import *
import tkinter as ttk
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile(event):
    global file
    root.title("Untitled - Omega text-editor")
    file = None
    TextArea.delete(1.0, END)
def new_file():
    global file
    root.title("Untitled - Omega text-editor")
    file = None
    TextArea.delete(1.0, END)

def openFile(event):
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Omega text-editor")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()
def open_file():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Omega text-editor")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile(event):
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Omega text-editor")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
def save_file():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Omega text-editor")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp(event):
    root.destroy()
def quit_app():
    root.destroy()


        
def about():
    
    import tkinter as tk

    about=tk.Tk()
    about.title('About us')
    about.geometry('450x100')
    about.wm_iconbitmap('favicon.ico')
    t1=Label(about,text='Omega text-editor',font='helvetica 25')
    t1.pack()
    t2=Label(about,text='Omega text-editor is an editor for beginners',font='helvetica 15')
    t2.pack()

    
def light_theme():
    TextArea.config(bg="white", fg="black")
    f1.config(bg="white")
    
def dark_theme():
    color = '#1f1f1f'
    TextArea.config(bg="grey", fg="orange")
    f1.config(bg="black")
def getrow(event):
    index = textbox.index(INSERT)
    row = index.split(".")[0]
    print(row)
def ask():
    import tkinter as tk
    import tkinter as ttk
    ask=tk.Tk()
    ask.title('Select Theme')
    ask.wm_iconbitmap('favicon.ico')
    ask.geometry('250x250')
    
    
    Def_Btn = Button(ask, text='Dark theme off',borderwidth=1,bg='white',fg='black', command=light_theme)
    Def_Btn.pack(pady=50)
    Themed_Btn = ttk.Button(ask,text='Dark theme on',borderwidth=1,bg='black',fg='orange', command=dark_theme)
    Themed_Btn.pack()
    
    root.mainloop()
    
    
    
   



root = Tk()
root.geometry("1000x600")
root.config(bg="#CECCBE")
root.title("Untitled-Omega text-editor")
root.wm_iconbitmap('favicon.ico')
new_icon =PhotoImage(file='icons2/new.png')
open_icon =PhotoImage(file='icons2/open.png')

save_as_icon =PhotoImage(file='icons2/save_as.png')
exit_icon =PhotoImage(file='icons2/exit.png')
copy_icon = PhotoImage(file='icons2/copy.png')
paste_icon = PhotoImage(file='icons2/paste.png')
cut_icon = PhotoImage(file='icons2/cut.png')

f1 = Frame(root, bg="white", borderwidth=6, relief=FLAT)
f1.pack(side=LEFT, fill="y")
f2 = Frame(root, borderwidth=8, bg="light green", relief=FLAT)
f2.pack(side=TOP, fill="x")



root.bind('<Control-o>',openFile)
btn=Button(f1,image=open_icon,text="open",fg="black",bg="white",command=openFile)
root.bind('<Control-o>',openFile)
btn=Button(f1,image=open_icon,text="open",fg="black",bg="white",command=open_file)
btn.pack( pady=50)
root.bind('<Control-n>',newFile)
btn1=Button(f1,text="new",image=new_icon,fg="black",bg="white",command=newFile)
btn1=Button(f1,text="new",image=new_icon,fg="black",bg="white",command=new_file)
btn1.pack( pady=5)
root.bind('<Control-s>',saveFile)
btn2=Button(f1,text="save",image=save_as_icon,fg="black",bg="white",command=saveFile)

root.bind('<Control-s>',saveFile)
btn2=Button(f1,text="save",image=save_as_icon,fg="black",bg="white",command=save_file)
btn2.pack( pady=5)
root.bind('<Control-e>',quitApp)
btn3=Button(f1,text="exit",image=exit_icon,fg="black",bg="white",command=quitApp)

btn3=Button(f1,text="exit",image=exit_icon,fg="black",bg="white",command=quit_app)
btn3.pack( pady=5)

btn7=Button(f1,text="About us",fg="black",bg="white",command=about)
btn7.pack( pady=5)
l = Label(f2, text="Welcome to Omega text-editor", font="Helvetica 16 bold", fg="black",bg="light green", pady=22)
l.pack()
butn=Button(f1,text='Select Theme',command=ask)
butn.pack()
#Add TextArea
TextArea = Text(root, font="lucida 13")
file = None
TextArea.pack(expand=True, fill=BOTH)






#Adding Scrollbar using rules from Tkinter lecture no 22
Scroll = Scrollbar(TextArea)
Scroll.pack(side=RIGHT,  fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)

root.mainloop()
