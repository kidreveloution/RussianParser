from tkinter import *
from tkinter import ttk, Text
import tkinter as tk
from sentenceValid import *

root = Tk(className=' Epic Russian Parser')
root.geometry("900x700")

def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    result = sentenceValid(inp)
    lbl.config(text = result)


label=Label(root, text="Epic Russian Parser", font='Arial 17 bold')
label.place(relx=0.5, rely=0.1, anchor=CENTER)
label = Label(root, text="====================", font='Arial 17 bold')
label.place(relx=0.5, rely=0.2, anchor=CENTER)
label = Label(root, text="Word Bank", font='Arial 17 bold')
label.place(relx=0.5, rely=0.25, anchor=CENTER)

label = Label(root, text="Nouns\n\nMuzhshina(man) || Zhenshina(woman)\n Kot(cat) || Sabaka(dog)\n Gorod(city) || Djerjeva(tree)\nMashina(car) || Sestra(sister)\nStol(table) || Brat(brother)",
              font='Arial 17 bold', borderwidth=5, relief="solid")
label.place(relx=0.3, rely=0.4, anchor=E)

label = Label(root, text="Verbs \n\nZnat(to know) || Ljubit(to love)\nRabotat(to work) || Gavarit(to speak)\nDumat(to think) || Guljat(to walk)\nKhatjet(to want) || Djelat(to do)\nDavat(to give) || Idti(to go)",
              font='Arial 17 bold', borderwidth=5, relief="solid")
label.place(relx=0.5, rely=0.4, anchor=CENTER)

label = Label(root, text="Verbs \n\nZnat(to know) || Ljubit(to love)\nRabotat(to work) || Gavarit(to speak)\nDumat(to think) || Guljat(to walk)\nKhatjet(to want) || Djelat(to do)\nDavat(to give) || Idti(to go)",
              font='Arial 17 bold', borderwidth=5, relief="solid")
label.place(relx=0.5, rely=0.4, anchor=CENTER)

label = Label(root, text="Adjectives: \n\n Malenkiy(small) | | Balshoj(big)\nVysokiy(tall) | | Nizkiy(short)\nNoviy(new) | | Staryy(old)\nSilnyy(strong) | | Krasivyy(beautiful)\nBagatiy(rich) | | Zdaroviy(healthy)",
              font='Arial 17 bold', borderwidth=5, relief="solid")
label.place(relx=0.8, rely=0.4, anchor=CENTER)

label = Label(root, text="Prepositions And Conjunctions: \n\nv( in ) || na(on)\nmezhdu(between) || iz(from(place))\ns(with) || ot(from (person)\n\nee(and)(И)",
              font='Arial 17 bold', borderwidth=5, relief="solid")
label.place(relx=0.5, rely=0.6, anchor=CENTER)

inputtxt = tk.Text(
                   height = 3,
                   width = 60)
  
inputtxt.grid(columnspan=5,row=5,column=2)
inputtxt.place(relx=0.5, rely=0.8, anchor='center')

submitButton = ttk.Button(root, text="Submit Sentence", command=printInput)
submitButton.grid(columnspan=5,row=5,column=2)
submitButton.place(relx=0.5, rely=0.85, anchor='center')


lbl = tk.Label( text = "")
lbl.grid(columnspan=5,row=5,column=2)
lbl.place(relx=0.5, rely=0.9, anchor='center')
root.mainloop()

