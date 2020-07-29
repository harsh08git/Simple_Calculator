from tkinter import *

root = Tk()

#Set title for the main window
root.title("Simple Calculator")

#Set icon for main window
root.iconbitmap("Calculator_icon.ico")

#Creating the display for calculator
display = Entry(root, width=35, font=("Times New Roman",10,"bold"), justify="right")

def button_click(number):
    old_number = display.get()
    display.delete(0,last=END)
    new_number = str(old_number)+str(number)
    display.insert(0,new_number)

def del_num():
    display.delete(len(display.get())-1)

def clear_num():
    display.delete(0,last=END)

def addition():
    global num1
    try:
        num1 = int(display.get())
    except:
        num1 = float(display.get())
    clear_num()
    display.insert(0,str(num1)+" + ")
    global operation
    operation='+'

def subtraction():
    global num1
    try:
        num1 = int(display.get())
    except:
        num1 = float(display.get())
    clear_num()
    display.insert(0,str(num1)+" - ")
    global operation
    operation='-'

def multiplication():
    global num1
    try:
        num1 = int(display.get())
    except:
        num1 = float(display.get())
    clear_num()
    display.insert(0,str(num1)+" * ")
    global operation
    operation='*'

def division():
    global num1
    try:
        num1 = int(display.get())
    except:
        num1 = float(display.get())
    clear_num()
    display.insert(0,str(num1)+" / ")
    global operation
    operation='/'

def result():
    string = display.get()
    index = string.find(" ")
    try:
        num2 = int(string[index+3:])
    except:
        num2 = float(string[index+3:])
    clear_num()

    if operation == '+':
        display.insert(0,num1+num2)

    elif operation == '-':
        display.insert(0,num1-num2)

    elif operation == '*':
        display.insert(0,num1*num2)

    else:
        display.insert(0,float(num1/num2))

root.configure(background="black")

#Creating all buttons
B1 = Button(root, text="1",width=7,height=3,command=lambda: button_click(1),fg="#D7DADC",bg="#0C60AB")
B2 = Button(root, text="2",width=7,height=3,command=lambda: button_click(2),fg="#D7DADC",bg="#0C60AB")
B3 = Button(root, text="3",width=7,height=3,command=lambda: button_click(3),fg="#D7DADC",bg="#0C60AB")
B4 = Button(root, text="4",width=7,height=3,command=lambda: button_click(4),fg="#D7DADC",bg="#0C60AB")
B5 = Button(root, text="5",width=7,height=3,command=lambda: button_click(5),fg="#D7DADC",bg="#0C60AB")
B6 = Button(root, text="6",width=7,height=3,command=lambda: button_click(6),fg="#D7DADC",bg="#0C60AB")
B7 = Button(root, text="7",width=7,height=3,command=lambda: button_click(7),fg="#D7DADC",bg="#0C60AB")
B8 = Button(root, text="8",width=7,height=3,command=lambda: button_click(8),fg="#D7DADC",bg="#0C60AB")
B9 = Button(root, text="9",width=7,height=3,command=lambda: button_click(9),fg="#D7DADC",bg="#0C60AB")
B0 = Button(root, text="0",width=7,height=3,command=lambda: button_click(0),fg="#D7DADC",bg="#0C60AB")
B_equal =  Button(root,text="=",height=3,width=17,command=result,fg="#D7DADC",bg="#0C60AB")

B_dec = Button(root, text=".",width=7,height=3,command=lambda: button_click("."),fg="#D7DADC",bg="#394986")
B_clear = Button(root,text="Clear",height=3,width=17,command=clear_num,bg="#394986",fg="#D7DADC")
B_del = Button(root,text="del",height=3,width=7,command=del_num,bg="#394986",fg="#D7DADC")


#Operational Button
B_add = Button(root,text="+",height=3,width=7,command=addition,bg="#0D086D",fg="#D7DADC")
B_sub = Button(root,text="-",width=7,height=3,command=subtraction,bg="#0D086D",fg="#D7DADC")
B_mul = Button(root,text="*",width=7,height=3,command=multiplication,bg="#0D086D",fg="#D7DADC")
B_div = Button(root,text="/",width=7,height=3,command=division,bg="#0D086D",fg="#D7DADC")


#Placing the display widget
display.grid(row=0,column=0,columnspan=4,padx=10,pady=10,ipady=5)

#Placing all buttons
B7.grid(row=1,column=0,pady=2)
B8.grid(row=1,column=1,pady=2)
B9.grid(row=1,column=2,pady=2)
B_add.grid(row=1,column=3,pady=2)

B4.grid(row=2,column=0,pady=2)
B5.grid(row=2,column=1,pady=2)
B6.grid(row=2,column=2,pady=2)
B_sub.grid(row=2,column=3,pady=2)

B1.grid(row=3,column=0,pady=2)
B2.grid(row=3,column=1,pady=2)
B3.grid(row=3,column=2,pady=2)
B_mul.grid(row=3,column=3,pady=2)

B0.grid(row=4,column=0,pady=2)
B_div.grid(row=4,column=3,pady=2)
B_equal.grid(row=4,column=1,columnspan=2,pady=2)

B_dec.grid(row=5,column=0,pady=2)
B_clear.grid(row=5,column=1,columnspan=2,pady=2)
B_del.grid(row=5,column=3,pady=2)


root.mainloop()