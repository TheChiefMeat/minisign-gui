import os
import tkinter as tk
from tkinter import filedialog

# create the application and the main window
root = tk.Tk()
root.title("Minisign GUI")
root.minsize(500,100)
root.maxsize(500,100)

#Close program functions
def Close(): 
    root.destroy()
    create.destroy()
    
def CloseCreate():
    create.destroy()

#Creates Minisign key
def CreateKey():
    KeyString = e1.get()
    os.system('cmd /c "start "" minisign -G -p minisign-keys/"' + KeyString + '".pub -s minisign-keys/"' + KeyString + '".key"')

def Create():
    global create
    create = tk.Tk()
    create.title("Minisign GUI")
    create.minsize(322,26)
    create.maxsize(322,26)

    tk.Label(create, text="Enter Keyfile Name") .grid(row=0, column=0)

    global e1
    e1 = tk.Entry(create)
    e1.grid(row=0, column=1)

    #Creates a button, placed in create window
    tk.Button(create, text='Create', command=CreateKey) .grid(row=0, column=3)

    #Creates a button, placed in create window
    tk.Button(create, text='Cancel', command=CloseCreate) .grid(row=0, column=4)

#Select file for upload
def Select(event=None):
    global Keyfile
    Keyfile = filedialog.askopenfilename(filetypes=[("Minisign Public Key", "*.pub"), ("Minisign Private Key", "*.key")])
    print('Selected:', Keyfile)

def Sign():
    global SignedFile
    SignedFile = filedialog.askopenfilename(filetypes=[("Select file to sign", "*")])
    os.system('cmd /c "start "" minisign -Sm ' + '"' + SignedFile + '"' + ' -s ' + '"' + Keyfile + '"')
    print('Selected:', SignedFile)

#Verifies selected file
def Verify():
    global VerifyFile
    VerifyFile = filedialog.askopenfilename(filetypes=[("Select file to verify", "*")])
    os.system('cmd /k "minisign -Vm ' + '"' + VerifyFile + '"' + ' -p ' + '"' + Keyfile + '"')
    print('Selected:', VerifyFile)

#Creates a button, placed in root window
button = tk.Button(root, text='Cancel', command=Close)
button.pack(side="left", fill="both", expand="true")

#Creates a button, placed in root window
button = tk.Button(root, text='Create', command=Create)
button.pack(side="left", fill="both", expand="true")

#Creates a button, placed in root window
button = tk.Button(root, text='Select', command=Select)
button.pack(side="left", fill="both", expand="true")

#Creates a button, placed in root window
button = tk.Button(root, text='Sign', command=Sign)
button.pack(side="left", fill="both", expand="true")


#Creates a button, placed in root window
button = tk.Button(root, text='Verify', command=Verify)
button.pack(side="left", fill="both", expand="true")

#Below lines ensure program starts in the center of the screen

w = 500 # width for the Tk root
h = 100 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

# Shows Main Window
root.mainloop()