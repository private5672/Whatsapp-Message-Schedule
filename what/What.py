from tkinter import *
import pywhatkit
root = Tk()
root.wm_iconbitmap("icon/default.ico")
root.wm_title("Mscheduler")
#Function
def Function():
    n=Entry1.get()
    m=Entry2.get()
    L=Entry3.get()
    I=Entry4.get()
    y="+91"
    pywhatkit.sendwhatmsg(y+n,str(m),int(L),int(I))

#mainscreen
Canvas = Canvas(root, bg="#c2f0c2", height=250, width=1000)
Canvas.grid(row=0, column=4)

Label1 = Label(Canvas, text="Mscheduler by AD",bg='#99e6ff',font="Verdana 34", relief="solid", borderwidth=5)
Label1.grid(row=0,column=0)

Label2= Label(Canvas,text="Enter Phone no",bg="#c2f0c2",font="verdana 22")
Label2.grid(row=2 , column=0)

Entry1=Entry(Canvas,bg="#ffe6b3",font="verdana 22", relief="ridge", borderwidth=3)
Entry1.grid(row=2, column=1)

Label3= Label(Canvas,text="Enter Message",bg="#c2f0c2",font="verdana 22")
Label3.grid(row=3 , column=0)

Entry2=Entry(Canvas,bg="#ffe6b3",font="verdana 22", relief="ridge", borderwidth=3)
Entry2.grid(row=3, column=1)

Label4= Label(Canvas,text="     Hour",bg="#c2f0c2",font="verdana 22")
Label4.grid(row=4 , column=0)

Entry3=Entry(Canvas,bg="#ffe6b3",font="verdana 22", relief="ridge", borderwidth=3)
Entry3.grid(row=4, column=1)

Label5= Label(Canvas,text="     Minutes",bg="#c2f0c2",font="verdana 22")
Label5.grid(row=5 , column=0)

Entry4=Entry(Canvas,bg="#ffe6b3",font="verdana 22", relief="ridge", borderwidth=3)
Entry4.grid(row=5, column=1)

Button1=Button(Canvas, bg="#d1d1e0", text="send", font="verdana 18", command=Function)
Button1.grid(row=6, column=0)

root.mainloop()


