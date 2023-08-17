from tkinter import *
import random

root = Tk()
root.geometry("800x480")
root.title("Roll Dice")

label = Label(root, text="", font=("times new roman", 265))

def roll():
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.configure(text=f'{random.choice(dice)}{random.choice(dice)}{random.choice(dice)}')
    label.pack()

button = Button(root,text= "Click To Roll", width=30, height=4, font=10, bg="black", fg="white", bd=3, command=roll)
button.pack(padx=10, pady=10)

root.mainloop()