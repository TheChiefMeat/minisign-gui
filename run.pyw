import os
import tkinter as tk
from tkinter import filedialog

# create the application and the main window
root = tk.Tk()
root.minsize(400,100)
root.maxsize(400,100)

#Close program function
def Close(): 
    root.destroy()

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
button.pack()

#Creates a button, placed in root window
button = tk.Button(root, text='Select Key File', command=Keyfile)
button.pack()

#Creates a button, placed in root window
button = tk.Button(root, text='Enter', command=Enter)
button.pack()


# Shows Main Window
root.mainloop()