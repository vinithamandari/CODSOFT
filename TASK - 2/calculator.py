from tkinter import *

first_number=second_number=operator=None

def get_digit(digit):               #FUNCTIONS
    current = result_label['text']
    new=current + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')

def get_operator(op):
    global first_number,operator
    first_number =float(result_label["text"])
    operator=op
    result_label.config(text='')

def get_result():
    global first_number,second_number,operator
    second_number=float(result_label['text'])

    if operator=='+':
        result_label.config(text=str(first_number+second_number))
    elif operator == '-':
        result_label.config(text=str(first_number-second_number))
    elif operator == 'x':
        result_label.config(text=str(first_number*second_number))
    else :
        if second_number==0:
            result_label.config(text='Error')
        else:
            result_label.config(text=str((round(float(first_number)/second_number,7))))

root = Tk() #object

root.title("VM Calculator")         #title
root.geometry("270x525")            #size of the window
root.resizable(0,0)                 #window cannot be resizable
root.config(background= "black")

result_label = Label(root,text='',bg="black",fg="white")
result_label.grid(row=0,column=0,columnspan=10,pady=(50,25),sticky='w')
result_label.config(font=("Ariel",30,"bold"))

btn_AC = Button(root,text="AC",bg="gray39",fg="white",width=5,height=2,command=lambda :clear())
btn_AC.grid(row=1,column=0,pady=5)
btn_AC.config(font=("Ariel",14))

btn_arrow = Button(root,text="<-",bg="gray39",fg="white",width=5,height=2)
btn_arrow.grid(row=1,column=2,pady=5)
btn_arrow.config(font=("Ariel",14))

btn_addmul = Button(root,text="+/-",bg="gray39",fg="white",width=5,height=2)
btn_addmul.grid(row=1,column=3)
btn_addmul.config(font=("Ariel",14))

btn_div = Button(root,text="/",bg="gray39",fg="white",width=5,height=2,command=lambda:get_operator('/'))
btn_div.grid(row=1,column=4)
btn_div.config(font=("Ariel",14))

btn7 = Button(root,text="7",bg="gray25",fg="white",width=5,height=2,command=lambda:get_digit(7))
btn7.grid(row=2,column=0,pady=5)
btn7.config(font=("Ariel",14))

btn8 = Button(root,text="8",bg="gray25",fg="white",width=5,height=2,command=lambda:get_digit(8))
btn8.grid(row=2,column=2)
btn8.config(font=("Ariel",14))

btn9 = Button(root,text="9",bg="gray25",fg="white",width=5,height=2,command=lambda:get_digit(9))
btn9.grid(row=2,column=3)
btn9.config(font=("Ariel",14))

btn_mul = Button(root,text="x",bg="gray39",fg="white",width=5,height=2,command=lambda:get_operator('x'))
btn_mul.grid(row=2,column=4)
btn_mul.config(font=("Ariel",14))

btn4 = Button(root,text="4",bg="gray25",fg="white",width=5,height=2,command=lambda:get_digit(4))
btn4.grid(row=3,column=0,pady=5)
btn4.config(font=("Ariel",14))

btn5 = Button(root,text="5",bg="gray25",fg="white",width=5,height=2,command=lambda:get_digit(5))
btn5.grid(row=3,column=2,)
btn5.config(font=("Ariel",14))

btn6 = Button(root,text="6",bg="gray25",fg="white",width=5,height=2,command=lambda:get_digit(6))
btn6.grid(row=3,column=3)
btn6.config(font=("Ariel",14))

btn_sub = Button(root,text="-",bg="gray39",fg="white",width=5,height=2,command=lambda:get_operator('-'))
btn_sub.grid(row=3,column=4)
btn_sub.config(font=("Ariel",14))

btn1 = Button(root,text="1",bg="gray25",fg="white",width=5,height=2,command=lambda:get_digit(1))
btn1.grid(row=4,column=0,pady=5)
btn1.config(font=("Ariel",14))

btn2 = Button(root,text="2",bg="gray25",fg="white",width=5,height=2,command=lambda:get_digit(2))
btn2.grid(row=4,column=2,)
btn2.config(font=("Ariel",14))

btn3 = Button(root,text="3",bg="gray25",fg="white",width=5,height=2,command=lambda:get_digit(3))
btn3.grid(row=4,column=3)
btn3.config(font=("Ariel",14))

btn_add = Button(root,text="+",bg="gray39",fg="white",width=5,height=2,command=lambda:get_operator('+'))
btn_add.grid(row=4,column=4)
btn_add.config(font=("Ariel",14))

btn_per = Button(root,text="%",bg="gray25",fg="white",width=5,height=2,command=lambda:get_operator('%'))
btn_per.grid(row=5,column=0,pady=5)
btn_per.config(font=("Ariel",14))

btn0 = Button(root,text="0",bg="gray25",fg="white",width=5,height=2,command=lambda:get_digit(0))
btn0.grid(row=5,column=2)
btn0.config(font=("Ariel",14))

btn_dot = Button(root,text=".",bg="gray25",fg="white",width=5,height=2,command=lambda:get_digit('.'))
btn_dot.grid(row=5,column=3)
btn_dot.config(font=("Ariel",14))

btn_equal = Button(root,text="=",bg="gray39",fg="white",width=5,height=2,command=lambda :get_result())
btn_equal.grid(row=5,column=4)
btn_equal.config(font=("Ariel",14))


root.mainloop()