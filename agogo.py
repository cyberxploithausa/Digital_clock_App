from tkinter import *
import time
import sys

def lokaci():
    lokacin_yanzu = time.strftime("%H:%M:%S")
    agogo.config(text=lokacin_yanzu)
    agogo.after(200, lokaci)

root = Tk()
root.geometry("500x250")
root.title("Digital clock")
root.config(bg="ghost white")

digital_clock = Label(root, text="Digital Clock", font=("times", 24, "bold"))
digital_clock.grid(row=0, column=2)

agogo = Label(root, font=("times", 50, "bold"), bg="white")
agogo.grid(row=2, column=2, pady=25, padx=120)
lokaci()

notation = Label(root, text="Hours    Minutes   Seconds  ", font=("times", 15, "bold"))
notation.grid(row=3, column=2)



root.mainloop()