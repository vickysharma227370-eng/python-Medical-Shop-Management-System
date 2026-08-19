
import tkinter as tk

def click(event):
        global scvalue
        text= event.widget.cget("text")
        if text == "=":
            if scvalue.get().isdigit():
                value=int(scvalue.get())
            else:
                value=eval(screen.get())

            scvalue.set(value)
            screen.update()

        elif text == "C":
            scvalue.set("")
            screen.update()

        else:
            scvalue.set(scvalue.get() + text)
            screen.update()
cal=tk.Tk()
cal.geometry("470x500")
cal.title("Calculator")
scvalue=tk.StringVar()
scvalue.set("")
screen=tk.Entry(cal, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill="x",ipadx=8,pady=10,padx=10)

cfram=tk.Frame(cal,bg="grey")
btn=tk.Button(cfram,text="9",padx=28,pady=18,font="lucida 15 bold")
btn.pack(side="left",padx=16,pady=5)
btn.bind("<Button-1>",click)

btn=tk.Button(cfram,text="8",padx=28,pady=18,font="lucida 15 bold")
btn.pack(side="left",padx=18,pady=5)
btn.bind("<Button-1>",click)

btn=tk.Button(cfram,text="7",padx=28,pady=18,font="lucida 15 bold")
btn.pack(side="left",padx=18,pady=5)
btn.bind("<Button-1>",click)

btn=tk.Button(cfram,text="+",padx=28,pady=18,font="lucida 15 bold")
btn.pack(side="left",padx=18,pady=5)
btn.bind("<Button-1>",click)
cfram.pack()

cfram=tk.Frame(cal,bg="grey")
btn=tk.Button(cfram,text="6",padx=28,pady=18,font="lucida 15 bold")
btn.pack(side="left",padx=18,pady=5)
btn.bind("<Button-1>",click)

btn=tk.Button(cfram,text="5",padx=28,pady=18,font="lucida 15 bold")
btn.pack(side="left",padx=18,pady=5)
btn.bind("<Button-1>",click)

btn=tk.Button(cfram,text="4",padx=28,pady=18,font="lucida 15 bold")
btn.pack(side="left",padx=18,pady=5)
btn.bind("<Button-1>",click)

btn=tk.Button(cfram,text="-",padx=28,pady=18,font="lucida 15 bold")
btn.pack(side="left",padx=18,pady=5)
btn.bind("<Button-1>",click)
cfram.pack()

cfram=tk.Frame(cal,bg="grey")
btn=tk.Button(cfram,text="3",padx=28,pady=18,font="lucida 15 bold")
btn.pack(side="left",padx=17,pady=5)
btn.bind("<Button-1>",click)

btn=tk.Button(cfram,text="2",padx=28,pady=18,font="lucida 15 bold")
btn.pack(side="left",padx=18,pady=5)
btn.bind("<Button-1>",click)

btn=tk.Button(cfram,text="1",padx=28,pady=18,font="lucida 15 bold")
btn.pack(side="left",padx=18,pady=5)
btn.bind("<Button-1>",click)

btn=tk.Button(cfram,text="*",padx=28,pady=18,font="lucida 15 bold")
btn.pack(side="left",padx=18,pady=5)
btn.bind("<Button-1>",click)
cfram.pack()

cfram=tk.Frame(cal,bg="grey")
btn=tk.Button(cfram,text="C",padx=28,pady=18,font="lucida 15 bold")
btn.pack(side="left",padx=16,pady=5)
btn.bind("<Button-1>",click)

btn=tk.Button(cfram,text="0",padx=28,pady=18,font="lucida 15 bold")
btn.pack(side="left",padx=18,pady=5)
btn.bind("<Button-1>",click)

btn=tk.Button(cfram,text="/",padx=28,pady=18,font="lucida 15 bold")
btn.pack(side="left",padx=18,pady=5)
btn.bind("<Button-1>",click)

btn=tk.Button(cfram,text="=",padx=28,pady=18,font="lucida 15 bold")
btn.pack(side="left",padx=18,pady=5)
btn.bind("<Button-1>",click)
cfram.pack()

cal.mainloop()
