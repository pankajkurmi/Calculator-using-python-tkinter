from tkinter import *

root=Tk()
root.title("Calculator by pankaj")   #main title of the software


# input filed for displaying the values
inp= Entry(root,width=35,borderwidth=5)
inp.grid(row=0,column=0,columnspan=3,padx=10,pady=10)


#logic for operations
def Button_click(number):

    current=inp.get()
    inp.delete(0,END)
    inp.insert(0,str(current)+str(number))


def botton_clear():
    inp.delete(0,END)


def botton_equal():
    second_num=inp.get()
    inp.delete(0,END)
    if math=="addition":
        inp.insert(0,f_num+int(second_num))

    if math=="substraction":
        inp.insert(0,f_num-int(second_num))
    
    if math=="multiplication":
        inp.insert(0,f_num*int(second_num))
    
    if math=="division":
        inp.insert(0,f_num/int(second_num))
    

def botton_add():
    first_num=inp.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_num)
    inp.delete(0,END)

def botton_substract():
    
    first_num=inp.get()
    global f_num
    global math
    math="substraction"
    f_num=int(first_num)
    inp.delete(0,END)
    

def botton_multiplication():
    
    first_num=inp.get()
    global f_num
    global math
    math="multiplication"
    f_num=int(first_num)
    inp.delete(0,END)
    
def botton_divesion():
    
    first_num=inp.get()
    global f_num
    global math
    math="division"
    f_num=int(first_num)
    inp.delete(0,END)
    
#creating buttons

botton_1=Button(root,text="1",padx=40,pady=20,command=lambda:Button_click(1))
botton_2=Button(root,text="2",padx=40,pady=20,command=lambda:Button_click(2))
botton_3=Button(root,text="3",padx=40,pady=20,command=lambda:Button_click(3))
botton_4=Button(root,text="4",padx=40,pady=20,command=lambda:Button_click(4))
botton_5=Button(root,text="5",padx=40,pady=20,command=lambda:Button_click(5))
botton_6=Button(root,text="6",padx=40,pady=20,command=lambda:Button_click(6))
botton_7=Button(root,text="7",padx=40,pady=20,command=lambda:Button_click(7))
botton_8=Button(root,text="8",padx=40,pady=20,command=lambda:Button_click(8))
botton_9=Button(root,text="9",padx=40,pady=20,command=lambda:Button_click(9))
botton_0=Button(root,text="0",padx=40,pady=20,command=lambda:Button_click(0))


botton_add =            Button(root,text="+",    padx=39,pady=20,command=botton_add,fg="red")
botton_substract =      Button(root,text="-",    padx=39,pady=20,command=botton_substract,fg="red")
botton_multiplication = Button(root,text="*",    padx=39,pady=20,command=botton_multiplication,fg="red")
botton_divesion =       Button(root,text="/",    padx=39,pady=20,command=botton_divesion,fg="red")
botton_clear=           Button(root,text="Clear",padx=79,pady=20,command=botton_clear ,bg="red")
botton_equal=           Button(root,text="=",    padx=91,pady=20,command=botton_equal,fg="red",bg="black")


#fixing the position of the buttons

botton_1.grid(row=3,column=0)
botton_2.grid(row=3,column=1)
botton_3.grid(row=3,column=2)

botton_4.grid(row=2,column=0)
botton_5.grid(row=2,column=1)
botton_6.grid(row=2,column=2)

botton_7.grid(row=1,column=0)
botton_8.grid(row=1,column=1)
botton_9.grid(row=1,column=2)

botton_0.grid(row=4,column=0)


botton_clear.grid(row=5,column=1,columnspan=2)
botton_add.grid(row=5,column=0)
botton_equal.grid(row=4,column=1,columnspan=2)

botton_substract.grid(row=6,column=0)
botton_multiplication.grid(row=6,column=1)
botton_divesion.grid(row=6,column=2)


#looop for the loop statement
root.mainloop()