from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showerror

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def saveFile():
    global filename
    t = text.get(0.0, END)
    file1 = open(filename, "w")
    file1.write(t)
    file1.close()

def saveAs():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Oops!", message="Unable to save file...")


def openFile():
    f = filedialog.askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

def FontHelvetica():
    global text
    text.config(font="Helvetica")

def FontCourier():
    global text
    text.config(font="Courier")

def FontTimes():
    global text
    text.config(font="Times")

def FontArial():
    global text
    text.config(font="Arial")

root = Tk()
root.title("Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

text = Text(root, width=400, height=400)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As...", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

fontmenu = Menu(menubar)
fontmenu.add_command(label="Helvetica", command=FontHelvetica)
fontmenu.add_command(label="Courier", command=FontCourier)
fontmenu.add_command(label="Times", command=FontTimes)
fontmenu.add_command(label="Arial", command=FontArial)
menubar.add_cascade(label="Font", menu=fontmenu)


root.config(menu=menubar)
root.mainloop()