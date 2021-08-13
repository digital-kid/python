import os 
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import*
from tkinter import ttk
from tkinter import colorchooser
from tkinter import font
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
def saveFile():
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

            root.title(os.path.basename(file) + " - Hello-Pad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
def save2(event):
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

            root.title(os.path.basename(file) + " - Hello-Pad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()   


    
 
def cut():
    global selected
    if TextArea.selection_get():
        selected=TextArea.selection_get()
        TextArea.delete("sel.first","sel.last")
        root.clipboard_clear()
        root.clipboard_append(selected)
def find_func(event=None):

    def find():
        word = find_input.get()
        TextArea.tag_remove('match', '1.0',END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = TextArea.search(word, start_pos, stopindex=END)
                if not start_pos:
                    break 
                end_pos = f'{start_pos}+{len(word)}c'
                TextArea.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                TextArea.tag_config('match', foreground='white', background='blue')
    
    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = TextArea.get(1.0, END)
        new_content = content.replace(word, replace_text)
        TextArea.delete(1.0, END)
        TextArea.insert(1.0, new_content)
    
    find_dialogue = Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)
## frame 
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    ## labels
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text= 'Replace')

    ## entry 
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    ## button 
    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text= 'Replace', command=replace)

    ## label grid 
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    ## entry grid 
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)
    

    ## button grid 
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)
    find_dialogue.wm_iconbitmap('favicon.ico')
    find_dialogue.mainloop()
def new():
    global file
    root.title("Untitled - Hello-Pad")
    file = None
    TextArea.delete(1.0, END)
def new2(event):
    global file
    root.title("Untitled - Hello-Pad")
    file = None
    TextArea.delete(1.0, END)
def openfile():
          
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Hello-Pad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()
def open2(event):
          
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Hello-Pad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()
def font_color():
	my_color=colorchooser.askcolor()[1]
	if my_color:
		color_font=font.Font(TextArea,TextArea.cget("font"))
		
		status_bar.config(text=my_color)
		TextArea.tag_configure("colored",font=color_font,foreground=my_color)
		current_tags=TextArea.tag_names("sel.first")
		if "colored" in current_tags:
			TextArea.tag_remove("colored","sel.first","sel.last")
		else:
			TextArea.tag_add("colored","sel.first","sel.last")
def font_color2(event):
	color_font=font.Font(TextArea,TextArea.cget("font"))
	my_color=colorchooser.askcolor()[1]
	if my_color:
		
		status_bar.config(text=my_color)
		TextArea.tag_configure("colored",font=color_font,foreground=my_color)
		current_tags=TextArea.tag_names("sel.first")
		if "colored" in current_tags:
			TextArea.tag_remove("colored","sel.first","sel.last")
		else:
			TextArea.tag_add("colored","sel.first","sel.last")		
def bold_it():
	bold_font=font.Font(TextArea,TextArea.cget("font"))
	bold_font.configure(weight="bold")
	TextArea.tag_configure("bold",font=bold_font)
	current_tags=TextArea.tag_names("sel.first")
	if "bold" in current_tags:
		TextArea.tag_remove("bold","sel.first","sel.last")
	else:
		TextArea.tag_add("bold","sel.first","sel.last")
def bold_it2(event):
	bold_font=font.Font(TextArea,TextArea.cget("font"))
	bold_font.configure(weight="bold")
	TextArea.tag_configure("bold",font=bold_font)
	current_tags=TextArea.tag_names("sel.first")
	if "bold" in current_tags:
		TextArea.tag_remove("bold","sel.first","sel.last")
	else:
		TextArea.tag_add("bold","sel.first","sel.last")
def italic_it():
	italic_font=font.Font(TextArea,TextArea.cget("font"))
	italic_font.configure(slant="italic")
	TextArea.tag_configure("italic",font=italic_font)
	current_tags=TextArea.tag_names("sel.first")
	if "italic" in current_tags:
		TextArea.tag_remove("italic","sel.first","sel.last")
	else:
		TextArea.tag_add("italic","sel.first","sel.last")
def italic_it2(event):
	italic_font=font.Font(TextArea,TextArea.cget("font"))
	italic_font.configure(slant="italic")
	TextArea.tag_configure("italic",font=italic_font)
	current_tags=TextArea.tag_names("sel.first")
	if "italic" in current_tags:
		TextArea.tag_remove("italic","sel.first","sel.last")
	else:
		TextArea.tag_add("italic","sel.first","sel.last")
current_font_family = 'Arial'
current_font_size = 14
s=("sel.first","sel.last")
def change_font():
    global current_font_family
    current_font_family =font_family.get()
   	s.configure(font=(current_font_family, current_font_size))

def change_fontsize(event=None):
    global current_font_size
    current_font_size = size_var.get()
    TextArea.configure(font=(current_font_family, current_font_size))



root=Tk()
root.wm_iconbitmap('favicon.ico')
width, height = root.winfo_screenwidth(), root.winfo_screenheight()

root.geometry('%dx%d+0+0' % (width,height))
root.minsize(500,500)
root.title('Hello Pad')
toolbar=Frame(root,bg="white",borderwidth=10,relief=GROOVE)
toolbar.grid()
m = Menu(root, tearoff=0)
m.add_command(label="      Cut      CTRL+X",command=cut)
m.add_command(label="      Copy      CTRL+C",command=copy)
m.add_command(label="      Paste      CTRL+V",command=paste)
m.add_command(label="      Save      CTRL+S",command=saveFile)
m.add_command(label="      Find      CTRL+F",command=find_func)
m.add_command(label="      Exit      CTRL+E",command=exit)
m.add_command(label="      Open      CTRL+O",command=openfile)
m.add_command(label="      New      CTRL+N",command=new)
m.add_command(label="      Bold      CTRL+B",command=bold_it)
m.add_command(label="      Italic      CTRL+Q",command=italic_it)
m.add_command(label="      Underline      CTRL+U")
m.add_command(label="      Change Color      CTRL+M",command=font_color)
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
## font box 
font_tuple =font.families()
font_family =StringVar()
font_box =ttk.Combobox(toolbar, width=30, textvariable=font_family, state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=1, column=8, padx=5)


## size box 
size_var = IntVar()
font_size = ttk.Combobox(toolbar, width=14, textvariable = size_var, state='readonly')
font_size['values'] = tuple(range(8,81))
font_size.current(14)
font_size.grid(row=1, column=9, padx=5)
btnleft=Button(toolbar,image=left_icon)
btnleft.grid(column=2,row=2,padx=5)
btncenter=Button(toolbar,image=center_icon)
btncenter.grid(column=3,row=2,padx=5)
btnright=Button(toolbar,image=right_icon)
btnright.grid(column=4,row=2,padx=5)
savebtn=Button(toolbar,image=save_icon,command=saveFile)
savebtn.grid(column=0,row=1,padx=5)
findbtn=Button(toolbar,image=find_icon,command=find_func)
findbtn.grid(column=3,row=1,padx=5)
openbtn=Button(toolbar,image=open_icon,command=openfile)
openbtn.grid(column=0,row=2,padx=5)
fontbtn=Button(toolbar,image=font_icon,command=font_color)
fontbtn.grid(column=4,row=1,padx=5)
exitbtn=Button(toolbar,image=exit_icon,command=exit)
exitbtn.grid(column=5,row=1,padx=5)
newbtn=Button(toolbar,image=new_icon,command=new)
newbtn.grid(column=5,row=2,padx=5)
boldbtn=Button(toolbar,image=bold_icon,command=bold_it)
boldbtn.grid(column=6,row=1,padx=5)
italicbtn=Button(toolbar,image=italic_icon,command=italic_it)
italicbtn.grid(column=6,row=2,padx=5)
underlinebtn=Button(toolbar,image=underline_icon)
underlinebtn.grid(column=7,row=1,padx=5)
replacebtn=Button(toolbar,image=replace_icon,command=find_func)
replacebtn.grid(column=7,row=2,padx=5)
text=Label(toolbar,text="Welcome to Hello Pad      ",font="helvetica 43 italic",bg="white")
text.grid(column=10,row=1)
TextArea = Text(root, font="Helvetica 14")
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
root.bind("<Control-f>", find_func)
root.bind("<Control-s>", save2)
root.bind("<Control-h>",find_func)
root.bind("<Control-n>",new2)
root.bind("<Control-o>",open2)
root.bind("<Control-b>",bold_it2)
root.bind("<Control-q>",italic_it2)
root.bind("<Control-m>",font_color2)
root.bind("<Control-e>",exit2)
font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_fontsize)
root.mainloop()
