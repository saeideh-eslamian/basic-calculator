#------------Basic calculor-----------------


from tkinter import *

def buttom_press(num):

    global text_Calculator
    text_Calculator = text_Calculator + str(num)
    label_amounts.set(text_Calculator)


def equal():
    global text_Calculator

    try:
        total= str(eval(text_Calculator))
        label_amounts.set(total)

        text_Calculator = total
    except ZeroDivisionError:
       label_amounts.set("arithmetic error")
       text_Calculator = ""
    except SyntaxError:
        label_amounts.set("invalid syntax")
        text_Calculator = ""



def clear():
    global text_Calculator
    text_Calculator = ""
    label_amounts.set(text_Calculator)

window = Tk()
window.geometry("500x520")
window.title("Calculator")

text_Calculator=""
label_amounts = StringVar()

label_text = Label(window, textvariable=label_amounts, width="25", height="2", font = ("Arial",25), bg="white")
label_text.pack()

frame = Frame(window)
frame.pack()

buttom1 = Button(frame, height=4,width=9, text=1, font=20,
                 command= lambda: buttom_press(1))
buttom1.grid(row=0, column=0)

buttom2 = Button(frame, height=4,width=9, text=2, font=20,
                 command= lambda: buttom_press(2))
buttom2.grid(row=0, column=1)

buttom3 = Button(frame, height=4,width=9, text=3, font=20,
                 command= lambda: buttom_press(3))
buttom3.grid(row=0, column=2)

buttom4 = Button(frame, height=4,width=9, text=4, font=20,
                 command= lambda: buttom_press(4))
buttom4.grid(row=1, column=0)

buttom5 = Button(frame, height=4,width=9, text=5, font=20,
                 command= lambda: buttom_press(5))
buttom5.grid(row=1, column=1)

buttom6 = Button(frame, height=4,width=9, text=6, font=20,
                 command= lambda: buttom_press(6))
buttom6.grid(row=1, column=2)

buttom7 = Button(frame, height=4,width=9, text=7, font=20,
                 command= lambda: buttom_press(7))
buttom7.grid(row=2, column=0)

buttom8 = Button(frame, height=4,width=9, text=8, font=20,
                 command= lambda: buttom_press(8))
buttom8.grid(row=2, column=1)

buttom9 = Button(frame, height=4,width=9, text=9, font=20,
                 command= lambda: buttom_press(9))
buttom9.grid(row=2, column=2)

buttom0 = Button(frame, height=4,width=9, text=0, font=20,
                 command= lambda: buttom_press(0))
buttom0.grid(row=3, column=0)

sum = Button(frame, height=4,width=9, text="+", font=20,
                 command= lambda: buttom_press("+"))
sum.grid(row=0, column=3)

subtrac = Button(frame, height=4,width=9, text="-", font=20,
                 command= lambda: buttom_press("-"))
subtrac.grid(row=1, column=3)

decimal = Button(frame, height=4,width=9, text=".", font=20,
                 command= lambda: buttom_press("."))
decimal.grid(row=3, column=1)

multiply = Button(frame, height=4,width=9, text="*", font=20,
                 command= lambda: buttom_press("*"))
multiply.grid(row=2, column=3)


divided = Button(frame, height=4,width=9, text="/", font=20,
                 command= lambda: buttom_press("/"))
divided.grid(row=3, column=2)

equal = Button(frame, height=4,width=9, text="=", font=20,
                 command= equal)
equal.grid(row=3, column=3)

clear = Button(window, height=4,width=18, text="Clear", font=20,
                 command= clear)
clear.pack()



window.mainloop()
