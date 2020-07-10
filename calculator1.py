from tkinter import *
import time

root = Tk()
root.title("Rushil's  Calculator")

e = Entry(root, width=40 , borderwidth=50)
e.grid(row=0,column=0,columnspan=5,padx=50,pady=40)




##e.insert(0 ,"Enter your name")
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"  
    f_num = int(first_number)  
    e.delete(0, END)


def button_equal():
    second_number = e.get()    
    e.delete(0,END)
    
    if math == "addition" :             
        e.insert(0,f_num + int(second_number))


    if math == "substraction" :
        e.insert(0,f_num - int(second_number))

    if math == "multiplication" :
        e.insert(0,f_num * int(second_number))

    if math == "division" :
        e.insert(0,f_num / int(second_number))

    if math == "power" :
        e.insert(0,f_num ** int(second_number))

    if math == "root" :
        e.insert(0,f_num ** 0.5 )

    if math == "prcnt" :
        e.insert(0,f_num / 100 * float(second_number) )


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "substraction"  
    f_num = int(first_number)  
    e.delete(0,END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"  
    f_num = int(first_number)  
    e.delete(0,END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"  
    f_num = int(first_number)  
    e.delete(0,END)


def button_power():
    first_number = e.get()
    global f_num
    global math
    math = "power"  
    f_num = int(first_number)  
    e.delete(0,END)

def button_root():
    first_number = e.get()
    global f_num
    global math
    math = "root"  
    f_num = int(first_number)  
    e.delete(0,END)

def button_pct():
    first_number = e.get()
    global f_num
    global math
    math = "prcnt"  
    f_num = int(first_number)  
    e.delete(0,END)

button_1 = Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1),bg = 'light yellow' )
button_2 = Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2),bg = 'light yellow' )
button_3 = Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3),bg = 'light yellow' )
button_4 = Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4),bg = 'light yellow' )
button_5 = Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5),bg = 'light yellow' )
button_6 = Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6),bg = 'light yellow' )
button_7 = Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7),bg = 'light yellow' )
button_8 = Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8),bg = 'light yellow' )
button_0 = Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0),bg = 'light yellow' )
button_9 = Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9),bg = 'light yellow' )
button_add = Button(root,text="+",padx=40,pady=20,command=button_add,bg = 'yellow')
button_equal = Button(root,text="=",padx=40,pady=20,command=button_equal,bg = 'yellow')
button_clear = Button(root,text="⌫",padx=40,pady=20,command=button_clear,bg = 'yellow')
button_subtract = Button(root,text="-",padx=40,pady=20,command=button_subtract,bg = 'yellow')
button_multiply = Button(root,text="×",padx=40,pady=20,command=button_multiply,bg = 'yellow')
button_divide = Button(root,text="÷",padx=40,pady=20,command=button_divide,bg = 'yellow')
button_power = Button(root,text="         y\nX",padx=40,pady=20,command=button_power,bg = 'yellow')
button_root = Button(root,text=" 2√x ",padx=40,pady=20,command=button_root,bg = 'yellow')
button_pie = Button(root,text="  π  ",padx=40,pady=20,command=lambda: button_click(22/7),bg ='yellow' )
button_pct = Button(root,text=" % ",padx=40,pady=20,command=button_pct,bg = 'yellow')


button_pct.grid(row=1,column=1)
button_divide.grid(row=1,column=2)
button_pie.grid(row=1,column=3)
button_add.grid(row=1,column=4)


button_1.grid(row=2,column=1)
button_2.grid(row=2,column=2)
button_3.grid(row=2,column=3)
button_subtract.grid(row=2,column=4)

button_4.grid(row=3,column=1)
button_5.grid(row=3,column=2)
button_6.grid(row=3,column=3)
button_multiply.grid(row=3,column=4)

button_7.grid(row=4,column=1)
button_8.grid(row=4,column=2)
button_9.grid(row=4,column=3)
button_power.grid(row=4,column=4)

button_clear.grid(row=5,column=1)
button_0.grid(row=5,column=2)
button_equal.grid(row=5,column=3)
button_root.grid(row=5,column=4)


root.mainloop()