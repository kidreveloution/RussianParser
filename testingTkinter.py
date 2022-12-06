from tkinter import *

window = Tk()
# window.state("zoomed")
window.configure(bg="white")

def drag(event,origin_x,origin_y):
    x = event.x + event.widget.winfo_x()
    y = event.y + event.widget.winfo_y()
    event.widget.place(x=x, y=y, anchor="center")

card = Canvas(window, width=10, height=10, bg="blue")
card.place(x=50, y=50, anchor="center")
card.bind("<B1-Motion>", drag(50,50))

another_card = Canvas(window, width=10, height=10, bg="red")
another_card.place(x=100, y=50, anchor="center")
another_card.bind("<B1-Motion>", drag(100,50))

window.mainloop()