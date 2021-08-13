from tkinter import*
from tkinter import ttk
def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()
def exit():
    root.destroy()
def exit2(event):
    root.destroy()

def copy():
    TextArea.clipboard_clear()
    TextArea.clipboard_append(TextArea.selection_get())

     
def paste():
    global selected
    if selected:
        position=TextArea.index(INSERT)
        TextArea.insert(INSERT,TextArea.clipboard_get())
    


    
 
def cut():
    global selected
    if TextArea.selection_get():
        selected=TextArea.selection_get()
        TextArea.delete("sel.first","sel.last")
        root.clipboard_clear()
        root.clipboard_append(selected)
                
root=Tk()
root.wm_iconbitmap('favicon.ico')
width, height = root.winfo_screenwidth(), root.winfo_screenheight()

root.geometry('%dx%d+0+0' % (width,height))
root.minsize(500,500)
root.title('Omega Docs')
toolbar=Frame(root,bg="white",borderwidth=10,relief=GROOVE)
toolbar.grid()
m = Menu(root, tearoff=0)
m.add_command(label="      Cut      CTRL+X",command=cut)
m.add_command(label="      Copy      CTRL+C",command=copy)
m.add_command(label="      Paste      CTRL+V",command=paste)
m.add_command(label="      Save      CTRL+S")
m.add_command(label="      Find      CTRL+F")
m.add_command(label="      Exit      CTRL+E",command=exit)
m.add_command(label="      Open      CTRL+O")
m.add_command(label="      New      CTRL+N")
m.add_command(label="      Bold      CTRL+B")
m.add_command(label="      Italic      CTRL+I")
m.add_command(label="      Underline      CTRL+U")
m.add_command(label="      Change Color      CTRL+M")
font_icon =PhotoImage(file='icons3/fontcolor.png')
copy_icon =PhotoImage(file='icons3/copy.png')
paste_icon =PhotoImage(file='icons3/paste.png')
cut_icon =PhotoImage(file='icons3/cut.png')
left_icon =PhotoImage(file='icons3/alignleft.png')
center_icon =PhotoImage(file='icons3/aligncenter.png')
right_icon =PhotoImage(file='icons3/alignright.png')
open_icon =PhotoImage(file='icons3/open.png')
find_icon =PhotoImage(file='icons3/find.png')
save_icon =PhotoImage(file='icons3/save.png')
exit_icon =PhotoImage(file='icons3/exit.png')
new_icon =PhotoImage(file='icons3/new.png')
bold_icon =PhotoImage(file='icons3/bold.png')
italic_icon =PhotoImage(file='icons3/italic.png')
underline_icon =PhotoImage(file='icons3/underline.png')
replace_icon =PhotoImage(file='icons3/replace.png')
cutbtn=Button(toolbar,image=cut_icon,command=cut)
cutbtn.grid(row=1,column=1,pady=5)
copybtn=Button(toolbar,image=copy_icon,command=copy)
copybtn.grid(row=2,column=1,pady=5)
pastebtn=Button(toolbar,image=paste_icon,command=paste)
pastebtn.grid(row=1,column=2,padx=5)
clicked=StringVar()
clicked.set("Arial")
drop=OptionMenu(toolbar,clicked,"Cambria","Arial(Default)","Batang","BantangChe","Helvetica","ComaicSans MS")
drop.grid(column=8,row=1)
clickedint=IntVar()
clickedint.set("12")
dropsize=OptionMenu(toolbar,clickedint,"12","15","20","25","30","35","40")
dropsize.grid(column=9,row=1)
btnleft=Button(toolbar,image=left_icon)
btnleft.grid(column=2,row=2,padx=5)
btncenter=Button(toolbar,image=center_icon)
btncenter.grid(column=3,row=2,padx=5)
btnright=Button(toolbar,image=right_icon)
btnright.grid(column=4,row=2,padx=5)
savebtn=Button(toolbar,image=save_icon)
savebtn.grid(column=0,row=1,padx=5)
findbtn=Button(toolbar,image=find_icon)
findbtn.grid(column=3,row=1,padx=5)
openbtn=Button(toolbar,image=open_icon)
openbtn.grid(column=0,row=2,padx=5)
fontbtn=Button(toolbar,image=font_icon)
fontbtn.grid(column=4,row=1,padx=5)
exitbtn=Button(toolbar,image=exit_icon,command=exit)
exitbtn.grid(column=5,row=1,padx=5)
newbtn=Button(toolbar,image=new_icon)
newbtn.grid(column=5,row=2,padx=5)
boldbtn=Button(toolbar,image=bold_icon)
boldbtn.grid(column=6,row=1,padx=5)
italicbtn=Button(toolbar,image=italic_icon)
italicbtn.grid(column=6,row=2,padx=5)
underlinebtn=Button(toolbar,image=underline_icon)
underlinebtn.grid(column=7,row=1,padx=5)
replacebtn=Button(toolbar,image=replace_icon)
replacebtn.grid(column=7,row=2,padx=5)
text=Label(toolbar,text="Welcome to Omega-Docs          ",font="helvetica 43 italic",bg="white")
text.grid(column=10,row=1)
TextArea = Text(root, font="lucida 13")
file = None
TextArea.grid(row=3,rowspan=1,column=0, columnspan=4, sticky=N+S+W+E)
scrollb = ttk.Scrollbar(root, command=TextArea.yview)
scrollb.grid(row=3, column=1, sticky='nsew')
TextArea['yscrollcommand'] = scrollb.set

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
status_bar = ttk.Label(root, text = 'Status Bar')
status_bar.grid(row=4)

text_changed = False 
def changed(event=None):
    global text_changed
    if TextArea.edit_modified():
        text_changed = True 
        words = len(TextArea.get(1.0, 'end-1c').split())
        characters = len(TextArea.get(1.0, 'end-1c'))
        status_bar.config(text=f'Characters : {characters} Words : {words}')
    TextArea.edit_modified(False)

TextArea.bind('<<Modified>>', changed)
root.bind("<Button-3>", do_popup)

root.mainloop()
