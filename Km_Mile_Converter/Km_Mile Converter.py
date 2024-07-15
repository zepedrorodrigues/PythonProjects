from tkinter import Tk, Label, Entry, Radiobutton, IntVar, Button
def converter():
    option = int(r.get())
    distance = float(e.get().strip().replace(',' , '.'))
    measure1 = 'Miles'
    measure2 = 'Kilometers'
    if option ==1:
        measure1 = 'Miles'
        measure2 = 'Kilometers'
        final_distance = round(distance *1.609344,2)
    elif option ==2:
        measure1 = 'Kilometers'
        measure2 = 'Miles'
        final_distance = round(distance/1.609344,2)
    l_final = Label(text=f'{distance} {measure1}\n is equal to {final_distance} {measure2}')
    l_final.place(x=60,y=150)


w = Tk()
w.title('Km to Mile Converter')
w.minsize(100,200)

l = Label(text='Enter distance\nand select measure(right)',font=('Arial',12,'bold'))
l.grid(column=1,row=0)
l.config(padx=20, pady=10)

e = Entry()
e.grid(column=1,row=2)

r = IntVar()
r1=Radiobutton(text='Mls',value=1,variable=r)
r1.place(x=180,y=50)
r2=Radiobutton(text='Kms',value=2,variable=r)
r2.place(x=180,y=70)

b = Button(text='Click when finished!',command=converter)
b.place(x=60,y=100)

def __main__():
    w.mainloop()

while __name__=='__main__':
    __main__()