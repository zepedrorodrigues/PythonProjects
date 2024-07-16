from tkinter import PhotoImage, Tk, Button, Canvas

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("FlashCards")
window.geometry("800x500")
window.config(bg=BACKGROUND_COLOR)

frontImg = PhotoImage(file="images/card_front.png")
backImg = PhotoImage(file="images/card_back.png")
rightImg = PhotoImage(file="images/right.png")
wrongImg = PhotoImage(file="images/wrong.png")

canvas = Canvas(window, width=800, height=400, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_front_image = canvas.create_image(400, 200, image=frontImg)

buttonWrong = Button(image=wrongImg, highlightthickness=0)
buttonWrong.grid(row=1, column=0)

buttonRight = Button(image=rightImg, highlightthickness=0)
buttonRight.grid(row=1, column=1)

window.mainloop()
