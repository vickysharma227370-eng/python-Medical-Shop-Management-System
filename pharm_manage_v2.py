import subprocess as sp
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import sys
import mysql.connector

splash_root=tk.Tk()
splash_root.title("splash screen ")
splash_root.geometry("1366x768")

frame_s=tk.Frame(splash_root, border=15,bg="skyblue")
frame_s.place(width=1400, height=1366)

splash_label=tk.Label(frame_s,text=" MY MEDICAL SHOP",relief="raised", background="white",font=("Halvetica",30))
splash_label.pack(pady=200)

splash_label2=tk.Label(frame_s,text=" Project by ->AADIL, ASHUTOSH, VICKY",relief="raised",
                       background="white",font=("Halvetica",17))
splash_label2.pack(pady=120)

splash_label3=tk.Label(frame_s,text="Class 12A",relief="raised", background="white",font=("Halvetica",17))
splash_label3.place(x=650,y=605)


def main_window():
    import tkinter as tk
    
    splash_root.destroy()
    
    window=tk.Tk()
    window.title("MEDICAL SHOP")
    window.geometry("1360x710+-5+0")
    window.resizable(False,False)

    bno_var=tk.StringVar()
    men_var=tk.StringVar()
    price_var=tk.StringVar()
    exp_var=tk.StringVar()
    type_var=tk.StringVar()
    mfg_var=tk.StringVar()
    quan_var=tk.StringVar()

    ubno=tk.StringVar()
    umen=tk.StringVar()
    uprice=tk.StringVar()
    uexp=tk.StringVar()
    utype=tk.StringVar()
    umfg=tk.StringVar()
    uquan=tk.StringVar()
    
    def add_record():
        global count
        table.insert(parent="",index="end",iid=count,text="",values=(ebn.get(),emedn.get(),ogpri.get(),
expen.get(),etype.get(),exmfg.get(),equan.get()))
        count+=1

        conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="test")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into mede(batch,name,exp,price,type,mfg,quantity) values(%s,%s,%s,%s,%s,%s,%s)",(bno_var.get(),
                                                                                                       men_var.get(),
                                                                                                       price_var.get(),
                                                                                                       exp_var.get(),
                                                                                                       type_var.get(),
                                                                                                       mfg_var.get(),
                                                                                                       quan_var.get()
            ))
        conn.commit()
        conn.close()
        fetch_data()
        messagebox.showinfo("success","Medicine Added")
        
        ebn.delete("0","end")
        emedn.delete("0","end")
        ogpri.delete("0","end")
        expen.delete("0","end")
        etype.set(value="")
        exmfg.delete("0","end")
        equan.delete("0","end")

    def fetch_data():
        conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="test")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from mede")
        row=my_cursor.fetchall()
        if len(row)!=0:
            table.delete(*table.get_children())
            for i in row:
               table.insert("","end",values=i)
            conn.commit()
        conn.close()

    def remove_oa():
        a=table.selection()
        for record in a:
            table.delete(record)
        
        ba=ebnu.get()
        conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="test")
        my_cursor=conn.cursor()
        sql="delete from mede where batch=%s"
        val=(ba,)
        my_cursor.execute(sql,val)
        conn.commit()
        
        conn.close()
        
        fetch_data()
        messagebox.showinfo("Delete","Data deleted successfully")
        ebnu.delete("0","end")
        emednu.delete("0","end")
        ogpriu.delete("0","end")
        expenu.delete("0","end")
        etypeu.set(value="")
        exmfgu.delete("0","end")
        quanu.delete("0","end")
            
    def update_bt():
        selected=table.focus()
        table.item(selected,values=(ebnu.get(),emednu.get(),ogpriu.get(),expenu.get(),etypeu.get(),exmfgu.get(),quanu.get()))
        a=ubno.get()
        b=umen.get()
        c=uexp.get()
        d=uprice.get()
        e=utype.get()
        f=umfg.get()
        g=quanu.get()
        conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="test")
        my_cursor=conn.cursor()
        updateu="UPDATE mede SET name=%s,price=%s,exp=%s,type=%s,mfg=%s,quantity=%s WHERE batch=%s"
        val=(b,c,d,e,f,g,a)
        my_cursor.execute(updateu,val)
        conn.commit()
        
        fetch_data()
        messagebox.showinfo("success","Medicine updated")
        
        ebnu.delete("0","end")
        emednu.delete("0","end")
        ogpriu.delete("0","end")
        expenu.delete("0","end")
        etypeu.set(value="")
        exmfgu.delete("0","end")
        quanu.delete("0","end")

    def get_time():
        timevar=time.strftime("%I:%M:%S %p  %m/%d/%Y  %A")
        clock.config(text=timevar)
        clock.after(200,get_time)

    def select_d(e):
        ebnu.delete("0","end")
        emednu.delete("0","end")
        ogpriu.delete("0","end")
        expenu.delete("0","end")
        etypeu.set(value="")
        exmfgu.delete("0","end")
        quanu.delete("0","end")
        
        selected=table.focus()
        values=table.item(selected,"values")

        ebnu.insert(0,values[0])
        emednu.insert(0,values[1])
        expenu.insert(0,values[2])
        ogpriu.insert(0,values[3])
        etypeu.set(value=values[4])
        exmfgu.insert(0,values[5])
        quanu.insert(0,values[6])

    def clear_option():
        for record in table.get_children():
            table.delete(record)
        conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="test")
        my_cursor=conn.cursor()
        sql="truncate table mede"
        my_cursor.execute(sql)
        conn.commit()
        fetch_data()
        conn.close()
        
        ebnu.delete("0","end")
        emednu.delete("0","end")
        ogpriu.delete("0","end")
        expenu.delete("0","end")
        etypeu.set(value="")
        exmfgu.delete("0","end")
        quanu.delete("0","end")
        
        messagebox.showinfo("Clear","Data cleared successfully")

    def calc():
        cmd="python calculator.py"
        p=sp.Popen(cmd,shell=True)

    #title 
    e=tk.Label(window,text=" MY MEDICAL SHOP ", border=5, relief="ridge", background="white", foreground="royalblue",
    font=("times new roman",20,"bold"))
    e.place(x=0,y=0,width=1357,height=70)
    #mainframe
    dframe=tk.Frame(window, border=15,relief="ridge",padx=10,bg="skyblue")
    dframe.place(x=0,y=70, width=530, height=370)
    
    
    #left frame inside mainframe
    dframeleft=tk.LabelFrame(dframe,bd=7,bg="white",
                             relief="ridge",text="options",font=("courier new",17))
    dframeleft.place(x=-9,y=1, width=200, height=340)
    
    #right frame inside mainframe
    dframeright=tk.LabelFrame(dframe,bd=7,bg="white",
                              relief="ridge",text="Medicine entry",font=("courier new",17))
    dframeright.place(x=190,y=1, width=300, height=340)
    
    #mainframe2
    bframe=tk.Frame(window,border=7,bg="skyblue", relief="groove")
    bframe.place(x=530,y=70, width=830, height=305)

    #1 frame inside mainframe2
    bframeleft1=tk.LabelFrame(bframe,bd=7,bg="white")
    bframeleft1.place(x=0,y=1, width=160, height=290)

    #2 frame insde mainframe2
    bframeleft=tk.LabelFrame(bframe,bd=7,bg="white",
                             relief="ridge",text="options",font=("courier new",17))
    bframeleft.place(x=160,y=1, width=200, height=290)
    
    #3 frame inside mainframe2
    bframeright=tk.LabelFrame(bframe,bd=7,bg="white",
                              relief="ridge",text="Medicine Update",font=("courier new",17))
    bframeright.place(x=360,y=1, width=300, height=290)

    #4 frame inside mainframe2
    bframerightb=tk.LabelFrame(bframe,bd=7,bg="white",
                              relief="ridge",text="Data\noption",font=("courier new",15))
    bframerightb.place(x=660,y=1, width=153, height=290)

    #mainframe3
    clockframe=tk.Frame(window,border=7,bg="white",relief="ridge")
    clockframe.place(x=530,y=375, width=827, height=60)

    
    #######mainframe1 option########
    
    #######option######
    #b. no
    bno=tk.Label(dframeleft,bg="white",fg="red",text="B.No. :",font=("courier new",14))
    bno.grid(row=1, column=1,padx=40,pady=5)
    
    #medic name
    medname=tk.Label(dframeleft,bg="white",fg="red",text="Medicine name:",font=("courier new",14))
    medname.grid(row=2, column=1,pady=5)
    
    #ogprice
    pricog=tk.Label(dframeleft,bg="white",fg="red",text="Price :",font=("courier new",14))
    pricog.grid(row=3, column=1,pady=5)
    
    #expiry date
    exp=tk.Label(dframeleft,bg="white",fg="red",text="Expiry Date :",font=("courier new",14))
    exp.grid(row=4, column=1,pady=5)
    
    #type of medicine
    tymed=tk.Label(dframeleft,bg="white",fg="red",text="Medicine Type:",font=("courier new",14))
    tymed.grid(row=5, column=1,pady=5)
    
    # manufacturing date
    mdate=tk.Label(dframeleft,bg="white",fg="red",text="Mfg. date :",font=("courier new",14))
    mdate.grid(row=6, column=1,pady=5)

    #quantity
    quan=tk.Label(dframeleft,bg="white",fg="red",text="Quantity:",font=("courier new",14))
    quan.grid(row=7, column=1,pady=5)

    ########entry######
    
    #b.no. entry 
    ebn=tk.Entry(dframeright,textvariable=bno_var,width=43)
    ebn.grid(row=1,column=1,padx=7,pady=9)
    
    #medname entry 
    emedn=tk.Entry(dframeright,textvariable=men_var,width=43)
    emedn.grid(row=2,column=1,pady=11)
    
    #original price entry
    ogpri=tk.Entry(dframeright,textvariable=price_var,width=43)
    ogpri.grid(row=4,column=1,pady=11)
    
     # expiry date entry 
    expen=tk.Entry(dframeright,textvariable=exp_var,width=43)
    expen.grid(row=3,column=1,pady=6)
    
    #medicine type
    etype=ttk.Combobox(dframeright,textvariable=type_var,width=40,state="readonly")
    etype["values"]=("","TABLET","LIQUID","CAPSULE","DROPS")
    etype.current(0)
    etype.grid(row=5,column=1,pady=6)
    
    #mfg date
    exmfg=tk.Entry(dframeright,textvariable=mfg_var,width=43)
    exmfg.grid(row=6, column=1,pady=10)

    #quantity
    equan=tk.Entry(dframeright,textvariable=quan_var,width=43)
    equan.grid(row=7, column=1,pady=7)
    
    #add button
    addbutton=tk.Button(dframeright,text="add",width=20,height=2,command=lambda:add_record())
    addbutton.place(x=60,y=262)
    
   
    
    ########mainframe 2 option########
    ###bframe####

    #about
    aboutb=tk.Label(bframeleft1,text="APP INFO",width=20,height=2)
    aboutb.pack()

    aboutl=tk.Label(bframeleft1,text="""THIS IS A PROJECT\nMADE BY\n AADIL KHAN,\nVICKY SHARMA,\nASHUTOSH PANDAY
\nSTUDENTS OF \nCLASS 12 A \nKENDRIYA\nVIDYALAYA\nAMBIKAPUR\n\nTHANK YOU\nFOR USING THIS\nPROGRAM\n\n"""
                    ,font=("cambria",10),width=20)
    aboutl.place(x=0,y=30)

    #b. no
    bnou=tk.Label(bframeleft,bg="white",fg="red",text="B.No. :",font=("courier new",14))
    bnou.grid(row=1, column=1,padx=40,pady=7)
    
    #medic name
    mednameu=tk.Label(bframeleft,bg="white",fg="red",text="Medicine name:",font=("courier new",14))
    mednameu.grid(row=2, column=1,pady=4)
    
    #ogprice
    pricogu=tk.Label(bframeleft,bg="white",fg="red",text="Price:",font=("courier new",14))
    pricogu.grid(row=3, column=1,pady=4)
    
    #expiry date
    expu=tk.Label(bframeleft,bg="white",fg="red",text="Expiry Date:",font=("courier new",14))
    expu.grid(row=4, column=1,pady=4)
    
    #type of medicine
    tymedu=tk.Label(bframeleft,bg="white",fg="red",text="Medicine Type:",font=("courier new",14))
    tymedu.grid(row=5, column=1,pady=4)
      
    # manufacturing date
    mdateu=tk.Label(bframeleft,bg="white",fg="red",text="Mfg. date :",font=("courier new",14))
    mdateu.grid(row=6, column=1,pady=4)

    #quantity
    quanu=tk.Label(bframeleft,bg="white",fg="red",text="Quantity :",font=("courier new",14))
    quanu.grid(row=7, column=1,pady=4)

    #clock
    clock=tk.Label(clockframe,font=("Calibri",28),bg="white",fg="black")
    clock.place(x=140,y=0,height=45)
    #update entry
    
    #b.no. entry 
    ebnu=tk.Entry(bframeright,textvariable=ubno,width=41)
    ebnu.grid(row=1,column=1,padx=7,pady=7)
    
    #medname entry 
    emednu=tk.Entry(bframeright,textvariable=umen,width=41)
    emednu.grid(row=2,column=1,pady=12)
    
    #original price entry
    ogpriu=tk.Entry(bframeright,textvariable=uprice,width=41)
    ogpriu.grid(row=4,column=1,pady=12)
    
     # expiry date entry 
    expenu=tk.Entry(bframeright,textvariable=uexp,width=41)
    expenu.grid(row=3,column=1,pady=6)
    
    #medicine type
    etypeu=ttk.Combobox(bframeright,textvariable=utype,width=38,state="readonly")
    etypeu["values"]=("","TABLET","LIQUID","CAPSULE","DROPS")
    etypeu.current(0)
    etypeu.grid(row=5,column=1,pady=5)
    
    #mfg date
    exmfgu=tk.Entry(bframeright,textvariable=umfg,width=41)
    exmfgu.grid(row=6, column=1,pady=11)

    #quantity
    quanu=tk.Entry(bframeright,textvariable=uquan,width=41)
    quanu.grid(row=7, column=1,pady=4)

    #remove button
    removebutton=tk.Button(bframerightb,text="Remove",foreground="red",font=("Halvetica",9),width=18,height=3,command=remove_oa)
    removebutton.place(x=1,y=5)

    #update button
    updatebutton=tk.Button(bframerightb,text="Update",font=("Halvetica",9),width=18,height=3,command=update_bt)
    updatebutton.place(x=1,y=62)

    #clear button
    clear_button=tk.Button(bframerightb,text="Clear",foreground="red",font=("Halvetica",9),width=18,height=3,command=clear_option)
    clear_button.place(x=1,y=119)

    calc_button=tk.Button(bframerightb,text="Calculator",foreground="green",font=("Halvetica",9),width=18,height=3,command=calc)
    calc_button.place(x=1,y=176)
    
    #table
    table_frame=ttk.Frame(window,relief="groove")
    table_frame.place(x=0,y=437,width=1360,height=260)

    #scroll bar
    rtable_scroll=ttk.Scrollbar(table_frame)
    rtable_scroll.pack(side="right",fill="y")
    

    tlable=tk.Label(table_frame,bg="white",text="YOUR DATA",font="gadugi")
    tlable.place(x=0,y=0,width=1345)

    #data table
    table=ttk.Treeview(table_frame,column=("first","sec","third","forth","fifth","sixth","sev"),
                       show="headings",yscrollcommand=rtable_scroll.set)
       
    table.heading("first", text="B.NO")
    table.heading("sec", text="NAME")
    table.heading("third", text="PRICE")
    table.heading("forth", text="EXPIRY DATE")
    table.heading("fifth", text="TYPE")
    table.heading("sixth", text="MANUFACTURING DATE")
    table.heading("sev", text="QUANTITY")

    table.column("first",width=60,minwidth=60)
    table.column("sec",width=120,minwidth=120)
    table.column("third",width=70,minwidth=70)
    table.column("forth",width=100,minwidth=100)
    table.column("fifth",width=60,minwidth=60)
    table.column("sixth",width=100,minwidth=100)
    table.column("first",width=40,minwidth=40)

    data=[]

    global count
    count=0
    for record in data:
          count+=1

    table.place(x=0,y=20, height=238,width=1345)

    rtable_scroll.config(command=table.yview)

    table.bind("<ButtonRelease-1>",select_d)
    fetch_data()
    get_time()
splash_root.after(0000,main_window)

splash_root.mainloop()
