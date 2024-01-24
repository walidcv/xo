
from tkinter import *



#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
window = Tk()
window["background"]= "#42f5dd"
window.title(' X,O لعبة ')
window.geometry("475x660+1+1")
liss = ["x","o","x","o","x","o","x","o","x"]
def s():
    if btn1["text"] == "x" and btn2["text"] == "x" and btn3["text"] == "x":
        btn1["fg"]= 'red'
        btn2["fg"] = 'red'
        btn3["fg"] = 'red'
        window.title("finish")
        lbl["text"]="انتهت اللعبة "
        lbl2["text"] = "مبروووووك"

    elif btn1["text"] == "x" and btn5["text"] == "x" and btn9["text"] == "x" or btn1["text"] == "o" and btn5["text"] == "o" and btn9["text"] == "o":
        btn1["fg"] = 'red'
        btn5["fg"] = 'red'
        btn9["fg"] = 'red'
        window.title("finish")
        lbl["text"] = "انتهت اللعبة "
        lbl2["text"] = "مبروووووك"
    elif btn3["text"] == "x" and btn5["text"] == "x" and btn7["text"] == "x" or btn3["text"] == "o" and btn5["text"] == "o" and btn7["text"] == "o":
        btn3["fg"] = 'red'
        btn5["fg"] = 'red'
        btn7["fg"] = 'red'
        window.title("finish")
        lbl["text"] = "انتهت اللعبة "
        lbl2["text"] = "مبروووووك"
    elif btn4["text"] == "x" and btn5["text"] == "x" and btn6["text"] == "x" or btn4["text"] == "o" and btn5["text"] == "o" and btn6["text"] == "o":
        btn4["fg"] = 'red'
        btn5["fg"] = 'red'
        btn6["fg"] = 'red'
        window.title("finish")
        lbl["text"] = "انتهت اللعبة "
        lbl2["text"] = "مبروووووك"
    elif btn7["text"] == "x" and btn8["text"] == "x" and btn9["text"] == "x" or btn7["text"] == "o" and btn8["text"] == "o" and btn9["text"] == "o":
        btn7["fg"] = 'red'
        btn8["fg"] = 'red'
        btn9["fg"] = 'red'
        window.title("finish")
        lbl["text"] = "انتهت اللعبة "
        lbl2["text"] = "مبروووووك"
    elif btn1["text"] == "x" and btn4["text"] == "x" and btn7["text"] == "x" or btn1["text"] == "o" and btn4["text"] == "o" and btn7["text"] == "o":
        btn1["fg"] = 'red'
        btn4["fg"] = 'red'
        btn7["fg"] = 'red'
        window.title("finish")
        lbl["text"] = "انتهت اللعبة "
        lbl2["text"] = "مبروووووك"
    elif btn3["text"] == "x" and btn6["text"] == "x" and btn9["text"] == "x" or btn3["text"] == "o" and btn6["text"] == "o" and btn9["text"] == "o":
        btn3["fg"] = 'red'
        btn6["fg"] = 'red'
        btn9["fg"] = 'red'
        window.title("finish")
        lbl["text"] = "انتهت اللعبة "
        lbl2["text"] = "مبروووووك"
    elif btn2["text"] == "x" and btn5["text"] == "x" and btn8["text"] == "x" or btn2["text"] == "o" and btn5["text"] == "o" and btn8["text"] == "o":
        btn2["fg"] = 'red'
        btn5["fg"] = 'red'
        btn8["fg"] = 'red'
        window.title("finish")
        lbl["text"] = "انتهت اللعبة "
        lbl2["text"] = "مبروووووك"
def chose1():
    btn1["text"]=str(liss[0])
    del liss[0]
    s()

def chose2():
    btn2["text"]=str(liss[0])
    del liss[0]
    s()
def chose3():
    btn3["text"]=str(liss[0])
    del liss[0]
    s()

def chose4():
    btn4["text"]=str(liss[0])
    del liss[0]
    s()

def chose5():
    btn5["text"]=str(liss[0])
    del liss[0]
    s()
def chose6():
    btn6["text"]=str(liss[0])
    del liss[0]
    s()
def chose7():
    btn7["text"]=str(liss[0])
    del liss[0]
    s()
def chose8():
    btn8["text"]=str(liss[0])
    del liss[0]
    s()
def chose9():
    btn9["text"]=str(liss[0])
    del liss[0]
    s()


btn1 = Button(window,text="",font=("impact",25) , command=chose1,bd=5)
btn1.grid(row=0 , column=0 , ipadx=50, ipady=50)
btn2 = Button(window,text="",font=("impact",25) , command=chose2,bd=5)
btn2.grid(row=0 , column=1, ipadx=50, ipady=50)
btn3 = Button(window,text="",font=("impact",25) , command=chose3,bd=5)
btn3.grid(row=0 , column=2, ipadx=50, ipady=50)
btn4 = Button(window,text="",font=("impact",25) , command=chose4,bd=5)
btn4.grid(row=1 , column=0, ipadx=50, ipady=50)
btn5 = Button(window,text="",font=("impact",25) , command=chose5,bd=5)
btn5.grid(row=1 , column=1, ipadx=50, ipady=50)
btn6 = Button(window,text="",font=("impact",25), command=chose6 ,bd=5)
btn6.grid(row=1 , column=2, ipadx=50, ipady=50)
btn7 = Button(window,text="",font=("impact",25) , command=chose7,bd=5)
btn7.grid(row=2 , column=0, ipadx=50, ipady=50)
btn8 = Button(window,text="",font=("impact",25) , command=chose8,bd=5 )
btn8.grid(row=2 , column=1, ipadx=50, ipady=50)
btn9 = Button(window,text="",font=("impact",25), command=chose9 )
btn9.grid(row=2 , column=2, ipadx=50, ipady=50)
lbl = Label(window,text="",font=("impact",22),fg="green")
lbl.grid(row= 3,column=1)
lbl2 = Label(window,text="",font=("impact",22),fg="green")
lbl2.grid(row= 3,column=2)


window.mainloop()
print(liss)