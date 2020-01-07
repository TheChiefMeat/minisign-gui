import os
import tkinter as tk
from tkinter import filedialog

# create the application and the main window
root = tk.Tk()
root.title("Minisign Verify")
root.minsize(400,100)
root.maxsize(400,100)

#Close program function
def Close(): 
    root.destroy()

#Creates Minisign key
def Create():
    #Need new window to select custom path and names for keyfile
    create = tk.Tk()
    create.title("Minisign Verify")
    create.minsize(324,26)
    create.maxsize(324,26)

    tk.Label(create, text="Enter Keyfile Name") .grid(row=0, column=0)

    e1 = tk.Entry(create)
    e1.grid(row=0, column=1)

    #Creates a button, placed in root window
    tk.Button(create, text='Create') .grid(row=0, column=3)

    #Creates a button, placed in root window
    tk.Button(create, text='Cancel') .grid(row=0, column=4)

    #os.system('cmd /k "start "" minisign -G"')
    root.mainloop()

#Select file for upload
def Keyfile(event=None):
    global filename
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

#Runs selected file
def Enter():
    os.system('cmd /c "start "" ' + r'"' + filename + '"')

#Creates a button, placed in root window
button = tk.Button(root, text='Cancel', command=Close)
button.pack(side="left", fill="both", expand="true")

#Creates a button, placed in root window
button = tk.Button(root, text='Create', command=Create)
button.pack(side="left", fill="both", expand="true")

#Creates a button, placed in root window
button = tk.Button(root, text='Select Key File', command=Keyfile)
button.pack(side="left", fill="both", expand="true")


#Creates a button, placed in root window
button = tk.Button(root, text='Enter', command=Enter)
button.pack(side="left", fill="both", expand="true")

# Shows Main Window
root.mainloop()