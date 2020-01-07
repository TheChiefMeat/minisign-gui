import os
import tkinter as tk
from tkinter import filedialog

# create the application and the main window
root = tk.Tk()
root.minsize(400,100)
root.maxsize(400,100)

#Select file for upload
def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

#Creates a button, placed in root window
button = tk.Button(root, text='Open', command=UploadAction)
button.pack()


# Shows Main Window
root.mainloop()