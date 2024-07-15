from tkinter import PhotoImage, Tk, Button, Canvas

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("FlashCards")
window.geometry("800x500")
window.grid()

frontImg = PhotoImage(file="images/card_front.png")
backImg = PhotoImage(file="images/card_back.png")
rightImg = PhotoImage(file="images/right.png")
wrongImg = PhotoImage(file="images/wrong.png")

buttonWrong = Button(image=wrongImg,highlightthickness=0)
buttonRight = Button(image=rightImg,highlightthickness=0)

canvas = Canvas(window,width=800,height=400)
canvas.grid(row=0,column=0,columnspan=2)
canvas.create_image()




window.mainloop()

