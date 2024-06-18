
import tkinter
from PIL import Image, ImageTk
import random

root = tkinter.Tk()
root.geometry('400x400')
root.title('Roll the Dice')

backline = tkinter.Label(root, text="")
backline.pack()

HeadingLabel = tkinter.Label(root, text="Hello from Kivotos",
                                fg = "white",
                                    bg = "#78a0c8",
                                    font = "G2-Sans-Serif 16 bold italic")
HeadingLabel.pack()

HeadingLabe2 = tkinter.Label(root, text="Dice Roller Mk1",
                                fg = "white",
                                    bg = "#78a0c8",
                                    font = "G2-Sans-Serif 12 bold italic")
HeadingLabe2.pack()

dice = ['Dice Roller/die1.png', 'Dice Roller/die2.png', 'Dice Roller/die3.png', 'Dice Roller/die4.png', 'Dice Roller/die5.png', 'Dice Roller/die6.png']
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

ImageLabel = tkinter.Label(root, image=DiceImage) # type: ignore
ImageLabel.image = DiceImage # type: ignore

ImageLabel.pack( expand=True)

root.mainloop()