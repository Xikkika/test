from tkinter import *
from tkinter.ttk import Radiobutton

window = Tk()
window.title("Школьный тест")
window.geometry('150x150')


def t1():
    def clicked():
        s = 0
        if selected1.get() == 2:
            s += 1
        if selected2.get() == 3:
            s += 1
        if selected3.get() == 5:
            s += 1
        if selected4.get() == 8:
            s += 1
        if selected5.get() == 9:
            s += 1
        if selected6.get() == 11:
            s += 1
        if selected7.get() == 14:
            s += 1
        if selected8.get() == 16:
            s += 1
        if selected9.get() == 17:
            s += 1
        if selected10.get() == 20:
            s += 1
        lbl.configure(text=f"{s} балл(а/ов)")

    window1 = Toplevel()
    window1.title("Математический тест")
    window1.geometry('300x500')
    selected1 = IntVar()
    selected2 = IntVar()
    selected3 = IntVar()
    selected4 = IntVar()
    selected5 = IntVar()
    selected6 = IntVar()
    selected7 = IntVar()
    selected8 = IntVar()
    selected9 = IntVar()
    selected10 = IntVar()

    lbl = Label(window1)
    lbl.grid(column=1, row=20)

    lbl1 = Label(window1, text="2+2")
    lbl1.grid(column=1, row=0)

    lbl2 = Label(window1, text="10-6")
    lbl2.grid(column=1, row=2)

    lbl3 = Label(window1, text="5*9")
    lbl3.grid(column=1, row=4)

    lbl4 = Label(window1, text="9*7")
    lbl4.grid(column=1, row=6)

    lbl5 = Label(window1, text="20/4")
    lbl5.grid(column=1, row=8)

    lbl6 = Label(window1, text="42/7")
    lbl6.grid(column=1, row=10)

    lbl7 = Label(window1, text="8+8*8-8/8")
    lbl7.grid(column=1, row=12)

    lbl8 = Label(window1, text="(72+28)/2")
    lbl8.grid(column=1, row=14)

    lbl9 = Label(window1, text="77+33")
    lbl9.grid(column=1, row=16)

    lbl10 = Label(window1, text="100-101")
    lbl10.grid(column=1, row=18)

    rad1 = Radiobutton(window1, text='2', value=1, variable=selected1)
    rad2 = Radiobutton(window1, text='4', value=2, variable=selected1)
    rad1.grid(column=0, row=1)
    rad2.grid(column=2, row=1)

    rad3 = Radiobutton(window1, text='4', value=3, variable=selected2)
    rad4 = Radiobutton(window1, text='16', value=4, variable=selected2)
    rad3.grid(column=0, row=3)
    rad4.grid(column=2, row=3)

    rad5 = Radiobutton(window1, text='45', value=5, variable=selected3)
    rad6 = Radiobutton(window1, text='14', value=6, variable=selected3)
    rad5.grid(column=0, row=5)
    rad6.grid(column=2, row=5)

    rad7 = Radiobutton(window1, text='2', value=7, variable=selected4)
    rad8 = Radiobutton(window1, text='63', value=8, variable=selected4)
    rad7.grid(column=0, row=7)
    rad8.grid(column=2, row=7)

    rad9 = Radiobutton(window1, text='5', value=9, variable=selected5)
    rad10 = Radiobutton(window1, text='80', value=10, variable=selected5)
    rad9.grid(column=0, row=9)
    rad10.grid(column=2, row=9)

    rad11 = Radiobutton(window1, text='6', value=11, variable=selected6)
    rad12 = Radiobutton(window1, text='35', value=12, variable=selected6)
    rad11.grid(column=0, row=11)
    rad12.grid(column=2, row=11)

    rad13 = Radiobutton(window1, text='15', value=13, variable=selected7)
    rad14 = Radiobutton(window1, text='71', value=14, variable=selected7)
    rad13.grid(column=0, row=13)
    rad14.grid(column=2, row=13)

    rad15 = Radiobutton(window1, text='86', value=15, variable=selected8)
    rad16 = Radiobutton(window1, text='50', value=16, variable=selected8)
    rad15.grid(column=0, row=15)
    rad16.grid(column=2, row=15)

    rad17 = Radiobutton(window1, text='110', value=17, variable=selected9)
    rad18 = Radiobutton(window1, text='100', value=18, variable=selected9)
    rad17.grid(column=0, row=17)
    rad18.grid(column=2, row=17)

    rad19 = Radiobutton(window1, text='1', value=19, variable=selected10)
    rad20 = Radiobutton(window1, text='-1', value=20, variable=selected10)
    rad19.grid(column=0, row=19)
    rad20.grid(column=2, row=19)

    btn = Button(window1, text="/////", command=clicked)
    btn.grid(column=1, row=21)

    window1.mainloop()


def t2():
    window2 = Toplevel()
    window2.title("Ребусы")
    window2.geometry('300x450')
    enter1 = StringVar()
    enter2 = StringVar()
    enter3 = StringVar()

    def clicked1():
        s = 0
        if enter1.get().lower() == 'лиса':
            s += 1
        if enter2.get().lower() == 'лес':
            s += 1
        if enter3.get().lower() == 'проход':
            s += 1
        points.configure(text=f"{s} балл(а/ов)")

    reb1 = PhotoImage(file="./reb1.png")
    reb2 = PhotoImage(file="./reb2.png")
    reb3 = PhotoImage(file="./reb3.png")

    reb1_entry = Entry(window2, textvariable=enter1)
    reb1_entry.grid(column=0, row=2)

    reb2_entry = Entry(window2, textvariable=enter2)
    reb2_entry.grid(column=0, row=4)

    reb3_entry = Entry(window2, textvariable=enter3)
    reb3_entry.grid(column=0, row=6)

    img1 = Label(window2, image=reb1)
    img1.grid(column=0, row=1)

    img2 = Label(window2, image=reb2)
    img2.grid(column=0, row=3)

    img3 = Label(window2, image=reb3)
    img3.grid(column=0, row=5)

    points = Label(window2)
    points.grid(column=0, row=7)

    button = Button(window2, text="/////", command=clicked1)
    button.grid(column=0, row=8)

    window2.mainloop()


btn1 = Button(window, text="Математический тест", command=t1)
btn2 = Button(window, text="Ребусы", command=t2)
btn1.grid(column=1, row=0)
btn2.grid(column=1, row=2)

window.mainloop()
