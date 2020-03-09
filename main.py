from tkinter import *

window = Tk()
window.geometry('350x200')
window.title("Welcome to LikeGeeks app")
window2 = Tk()
window2.geometry('350x200')
window2.title("Welcome to LikeGeeks app")

window2.withdraw()

def swap():
    window.withdraw()
    window2.deiconify()

def swap2():
    window.deiconify()
    window2.withdraw()

btn = Button(window, text="red", command= lambda: window.configure(bg = 'red'))
btn2 = Button(window, text="green", command= lambda: window.configure(bg = 'green'))
btn3 = Button(window, text="blue", command= lambda: window.configure(bg = 'blue'))
btn_hide = Button(window, text="Hide", command= swap)
btn_swap = Button(window2, text="back", command= swap2)

btn.grid(column=1, row=0)
btn2.grid(column=2, row=0)
btn3.grid(column=3, row=0)
btn_hide.grid(column=4, row=0)

btn_swap.grid(column=1, row=0)

window.mainloop()
window2.mainloop()
