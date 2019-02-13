import pymongo
from tkinter import *

Client1 = pymongo.MongoClient("mongodb://localhost:27017/")
Db = Client1["test"]
Col = Db["calculator"]

expr = ""
btnWidth = 5
#li = {}

def press(num):
    global expr
    expr = expr + str(num)
    equation.set(expr)

'''def rev():

    Col.insert_one(li)
    for i in Col:
        print(i)'''




def pressequal():
    try:
        global expr
        result = str(eval(expr))
        equation.set(result)
        expr = ""
    except:
        equation.set("error")
        expr = ""

def clear():
    global expr
    expr = ""
    equation.set("")





if __name__== "__main__":
    gui = Tk()
    gui.configure(background="pink")
    gui.title("Calculator")
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=19, ipadx=60)
    equation.set("")
    gui.geometry("300x300")
    '''calculation = Label(gui, textvariable=equation, width=btnWidth * 2)
    calculation.grid(row=0, column=0, columnspan=4)'''

    button1 = Button(gui, text='1',padx = '10',pady='15',fg='blue',bg='white', command = lambda : press(1),height = 1, width = btnWidth )
    button1.place(x = '10',y = '50')

    button2 = Button(gui, text='2',padx = '10',pady='15',fg='blue',bg='white', command = lambda : press(2),height = 1, width = btnWidth )
    button2.place(x = '80',y = '50')

    button3 = Button(gui, text='3',padx = '10',pady='15',fg='blue',bg='white', command = lambda : press(3),height = 1, width = btnWidth)
    button3.place(x='150', y='50')

    buttonpl = Button(gui, text='+',padx = '10',pady='15',fg='blue',bg='white', command = lambda : press('+'),height = 1, width = btnWidth )
    buttonpl.place(x='220', y='50')

    button4 = Button(gui, text='4',padx = '10',pady='15',fg='blue',bg='white', command = lambda : press(4),height = 1, width = btnWidth)
    button4.place(x='10', y='100')

    button5 = Button(gui, text='5',padx = '10',pady='15',fg='blue',bg='white', command = lambda : press(5),height = 1, width = btnWidth )
    button5.place(x='80', y='100')

    button6 = Button(gui, text='6',padx = '10',pady='15',fg='blue',bg='white', command = lambda : press(6),height = 1, width = btnWidth )
    button6.place(x='150', y='100')

    buttonmi = Button(gui, text='-',padx = '10',pady='15',fg='blue',bg='white', command = lambda : press('-'),height = 1, width = btnWidth )
    buttonmi.place(x='220', y='100')

    button7 = Button(gui, text='7',padx = '10',pady='15',fg='blue',bg='white', command = lambda : press(7),height = 1, width = btnWidth)
    button7.place(x='10', y='150')

    button8 = Button(gui, text='8',padx = '10',pady='15',fg='blue',bg='white', command = lambda : press(8),height = 1, width = btnWidth )
    button8.place(x='80', y='150')

    button9 = Button(gui, text='9',padx = '10',pady='15',fg='blue',bg='white', command = lambda : press(9),height = 1, width = btnWidth )
    button9.place(x='150', y='150')

    buttonmu = Button(gui, text='*',padx = '10',pady='15',fg='blue',bg='white', command = lambda : press('*'),height = 1, width = btnWidth )
    buttonmu.place(x='220', y='150')

    buttonc = Button(gui, text='clear',padx = '10',pady='15',fg='blue',bg='white', command =clear,height = 1, width = btnWidth )
    buttonc.place(x='10', y='200')

    button0 = Button(gui, text='0',padx = '10',pady='15',fg='blue',bg='white', command = lambda : press(0),height = 1, width = btnWidth)
    button0.place(x='80', y='200')

    buttoneq = Button(gui, text = '=',padx = '10',pady='15',fg='blue',bg='white', command=pressequal,height = 1, width = btnWidth)
    buttoneq.place(x='150', y='200')

    buttondi = Button(gui, text='/',padx = '10',pady='15',fg='blue',bg='white', command = lambda : press('/'),height = 1, width = btnWidth )
    buttondi.place(x='220', y='200')

    #buttonre = Button(gui, text='prev',padx = '10',pady='15',fg='blue',bg='white', command = rev,height = 1, width = btnWidth )
    #buttonre.place(x='150', y='250')



    gui.mainloop()
