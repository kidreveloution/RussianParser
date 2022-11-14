from tkinter import *
from tkinter import ttk, Text
import tkinter as tk

root = Tk(className=' Epic Russian Parser')
root.geometry("500x200")

def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Provided Input: "+inp)


label=Label(root, text="Epic Russian Parser", font='Arial 17 bold')
label.place(relx=0.5, rely=0.1, anchor=CENTER)
label=Label(root, text="Enter a text in Russian, I'll tell you if it's a valid sentance", font='Arial 12 bold')
label.place(relx=0.5, rely=0.3, anchor=CENTER)

inputtxt = tk.Text(
                   height = 3,
                   width = 60)
  
inputtxt.grid(columnspan=5,row=5,column=2)
inputtxt.place(relx=0.5, rely=0.5, anchor='center')

submitButton = ttk.Button(root, text="Submit Sentence", command=printInput)
submitButton.grid(columnspan=5,row=5,column=2)
submitButton.place(relx=0.5, rely=0.8, anchor='center')


lbl = tk.Label( text = "")
lbl.grid(columnspan=5,row=5,column=2)
lbl.place(relx=0.5, rely=0.9, anchor='center')
root.mainloop()

