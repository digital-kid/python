from tkinter import *
import tkinter as ttk
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile(event):
    global file
    root.title("Untitled - Notepad")
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
        root.title(os.path.basename(file) + " - Notepad")
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

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp(event):
    root.destroy()

def cut(event):
    TextArea.event_generate(("<>"))

def copy(event):
    TextArea.event_generate(("<>"))

def paste(event):
    TextArea.event_generate(("<>"))

def about():
    showinfo("Omega-Text-editor", '''Omega-Text-editor is a
Text-editor for beginners''')
def light_theme():
    TextArea.config(bg="white", fg="black")
    
    
def dark_theme():
    color = '#1f1f1f'
    TextArea.config(bg="black", fg="green")
    
def getrow(event):
    index = textbox.index(INSERT)
    row = index.split(".")[0]
    print(row)   

    
    
    
   



root = Tk()
root.geometry("1000x600")
root.config(bg="#CECCBE")
root.title("Untitled-Omega text-editor")
new_icon =PhotoImage(file='icons2/new.png')
open_icon =PhotoImage(file='icons2/open.png')

save_as_icon =PhotoImage(file='icons2/save_as.png')
exit_icon =PhotoImage(file='icons2/exit.png')
copy_icon = PhotoImage(file='icons2/copy.png')
paste_icon = PhotoImage(file='icons2/paste.png')
cut_icon = PhotoImage(file='icons2/cut.png')
on= PhotoImage(file='icons2/darkmodeof.png')
of = PhotoImage(file='icons2/darkmodeon.png')
f1 = Frame(root, bg="white", borderwidth=6, relief=FLAT)
f1.pack(side=LEFT, fill="y")
f2 = Frame(root, borderwidth=8, bg="light green", relief=FLAT)
f2.pack(side=TOP, fill="x")



root.bind('<Control-o>',openFile)
btn=Button(f1,image=open_icon,text="open",fg="black",bg="white",command=openFile)
btn.pack( pady=50)
root.bind('<Control-n>',newFile)
btn1=Button(f1,text="new",image=new_icon,fg="black",bg="white",command=newFile)
btn1.pack( pady=5)
root.bind('<Control-s>',saveFile)
btn2=Button(f1,text="save",image=save_as_icon,fg="black",bg="white",command=saveFile)
btn2.pack( pady=5)
root.bind('<Control-e>',quitApp)
btn3=Button(f1,text="exit",image=exit_icon,fg="black",bg="white",command=quitApp)
btn3.pack( pady=5)
root.bind('<Control-x>',cut)
btn4=Button(f1,text="cut",image=cut_icon,fg="black",bg="white",command=cut)
btn4.pack( pady=5)
root.bind('<Control-c>',copy)
btn5=Button(f1,text="copy",image=copy_icon,fg="black",bg="white",command=copy)
btn5.pack( pady=5)
root.bind('<Control-v>',paste)
btn6=Button(f1,text="paste",image=paste_icon,fg="black",bg="white",command=paste)
btn6.pack( pady=5)
btn7=Button(f1,text="About us",fg="black",bg="white",command=about)
btn7.pack( pady=5)
l = Label(f2, text="Welcome to Omega text-editor", font="Helvetica 16 bold", fg="black",bg="light green", pady=22)
l.pack()
Def_Btn = Button(f1, image=of, command=light_theme)
Def_Btn.pack()
Themed_Btn = ttk.Button(f1, image=on, command=dark_theme)
Themed_Btn.pack()
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
