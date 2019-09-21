from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os



def newFile():
    global File
    root.title('Untitled - Notepad')
    File = None
    textarea.delete(1.0,END)           #deleting from character number 0 from line 1 to end



def openFile():
    global File
    File = askopenfilename(defaultextension = ".txt",filetypes = [("All Files","*.*"),("Text Documents","*.txt")])

    if File == "":
        File = None
    else:
        root.title(os.path.basename(File)+ " - Notepad")
        textarea.delete(1.0,END)
        f = open(File,"r")
        textarea.insert(1.0,f.read())
        f.close()



def saveFile():
    global File
    if File == None:
        File = asksaveasfilename(initialfile = "Untitled.txt",defaultextension = ".txt",filetypes = [("All Files","*.*"),("Text File","*.txt")])

        if File == "":
            File = None
        else:
            #save as a new file
            f = open(File,"w")
            f.write(textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(File) + " - Notepad")
            tmsg.showinfo("Notification","File Saved")
    else:
        f = open(File,"w")
        f.write(textarea.get(1.0,END))
        f.close()
        root.title(os.path.basename(File) + " - Notepad")
        tmsg.showinfo("Notification", "File Saved")


def quitFile():
    root.destroy()



def cut():
    textarea.event_generate('<<Cut>>')


def copy():
    textarea.event_generate('<<Copy>>')


def paste():
    textarea.event_generate('<<Paste>>')


def about():

    tmsg.showinfo(title="Tkinter Notepad",message="Basix Text Editor for Daily use")






if __name__ == "__main__":
    root = Tk()
    root.geometry("1020x488")
    root.title('Untitled - Notepad')

    textarea = Text(root,font = "lucida 10")
    textarea.pack(expand = True,fill = "both")


    menubar = Menu(root)
    File = None
    Filemenu = Menu(menubar,tearoff= 0)
    Filemenu.add_command(label = "New",command = newFile)
    Filemenu.add_command(label = "Open",command = openFile)
    Filemenu.add_command(label = "Save",command = saveFile)
    Filemenu.add_separator()
    Filemenu.add_command(label = "Exit",command = quitFile)

    menubar.add_cascade(label = "File",menu = Filemenu)



    Editmenu = Menu(menubar,tearoff = 0)
    Editmenu.add_command(label = "Cut",command = cut)
    Editmenu.add_command(label = "Copy",command = copy)
    Editmenu.add_command(label = "Paste",command = paste)
    menubar.add_cascade(label = "Edit",menu = Editmenu)



    Helpmenu = Menu(menubar,tearoff = 0)
    Helpmenu.add_command(label= "About Notepad",command= about)
    menubar.add_cascade(label = "Help",menu = Helpmenu)

    root.config(menu = menubar)

#adding scrollbar
    Scroll = Scrollbar(textarea)
    Scroll.pack(side = RIGHT,fill= Y)
    textarea.config(yscrollcommand = Scroll.set)
    Scroll.config(command = textarea.yview)


    root.mainloop()