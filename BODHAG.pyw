from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("B.O.D.H.A.G.")
root.iconbitmap("icon.ico")
root.resizable(False,False)
result=[0,0,0,0,0]
result[0]=IntVar()
result[1]=IntVar()
result[2]=IntVar()
result[3]=IntVar()
result[4]=IntVar()


choice=IntVar()

def b2g(list1):
    gc=[]
    gc.append(list1[0])
    [gc.append((int(list1[i])+int(list1[i-1]))%2) for i in range(1,len(list1))]
    return str(''.join(str(x) for x in gc))

def b2d(list1):
    num=list1[::-1]
    d=[int(num[i])*(2**i) for i in range(len(num))]
    return sum(d)


def o2d(list1):
    num=list1[::-1]
    d=[int(num[i])*(8**i) for i in range(len(num))]
    return sum(d)


def h2d(list1):
    num=list1[::-1]
    hexa=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    d=[hexa.index(num[i])*(16**i) for i in range(len(num))]
    return sum(d)


def d2h(num):
    num=int(num)
    hexa=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    rem=[]
    while(num!=0):
        rem.append(num%16)
        num//=16
    rem=rem[::-1]
    return ''.join([str(hexa[rem[i]]) for i in range(len(rem))])


def d2b(num):
    num=int(num)
    rem=[]
    while(num>0):
        rem.append(num%2)
        num//=2
    rem=rem[::-1]
    return int(''.join([str(rem[i]) for i in range(len(rem))]))


def d2o(num):
    num=int(num)
    rem=[]
    while(num!=0):
        rem.append(num%8)
        num//=8
    rem=rem[::-1]
    return int(''.join([str(rem[i]) for i in range(len(rem))]))
   

def check():
    x=Number.get()
    list1=[x.upper() for x in str(x)]
    type=sorted(set(list1))
    global nsys
    nsys=[0,0,0,0]
    try:
        if(all(int(i) <2 for i in type)):
            nsys[0]=1

    except:
        nsys[0]=0
    try:
        #if((isinstance(i, int) for i in type) or any(i.isalpha() for i in type)):
        if(all(i in '0123456789abcdefABCDEF' for i in type)):
            nsys[3]=1

    except:
        nsys[3]=0
    try:
        if(all(int(i) <8 for i in type)):
            nsys[1]=1
    except:
        nsys[1]=0

    try:
        if(all(int(i) <10 for i in type)):
            nsys[2]=1
    except:
        nsys[2]=0

    if(sum(nsys)==0):
        response=messagebox.showerror("BODHAG", "Error 101:\nWrong Input")
        return
    
    if(nsys[0]):
        rb1.config(state=NORMAL)
        rb5.config(state=NORMAL)
    else:
        rb1.config(state=DISABLED)
        rb5.config(state=DISABLED)
        choice.set(1)
    if(nsys[1]):
        rb2.config(state=NORMAL)
    else:
        rb2.config(state=DISABLED)
        choice.set(2)
    if(nsys[2]):
        rb3.config(state=NORMAL)
    else:
        rb3.config(state=DISABLED)
        choice.set(3)
    if(nsys[3]):
        rb4.config(state=NORMAL)
    else:
        rb4.config(state=DISABLED)
    disable()
  
def disable():
    cb1.config(state=NORMAL)
    cb2.config(state=NORMAL)
    cb3.config(state=NORMAL)
    cb4.config(state=NORMAL)
    cb5.config(state=DISABLED)

    if choice.get() == 0:
        cb1.deselect()
        cb1.config(state=DISABLED)
        cb5.config(state=NORMAL)
    elif choice.get() == 1:
        cb2.deselect()
        cb2.config(state=DISABLED)
    elif choice.get() == 2:
        cb3.deselect()
        cb3.config(state=DISABLED)
    elif choice.get() == 3:
        cb4.deselect()
        cb4.config(state=DISABLED)
    elif choice.get() == 4:
        cb5.deselect()
        cb1.config(state=ACTIVE)
        cb2.config(state=DISABLED)
        cb3.config(state=DISABLED)
        cb4.config(state=DISABLED)

    
def convert():
    check()
    x=Number.get()
    list1=[x.upper() for x in str(x)]
    
    global Result
    try:
        Result.destroy()
    except:
        g=0
    Result=LabelFrame(root, text="Result", font=("Calibri",14), bg="#ffffbe", bd=3.5)
    Result.grid(row=5,column=0, padx=15, pady=(0,10), ipadx=5, ipady =5, columnspan=2, sticky=W+E)
    
    if(choice.get()==0):
        h=d2h(b2d(list1))
        o=d2o(b2d(list1))
        d=b2d(list1)
        g=b2g(list1)
    elif(choice.get()==1):
        b=d2b(o2d(list1))
        h=d2h(o2d(list1))
        d=o2d(list1)
    elif(choice.get()==2):
        b=b2d(list1)
        o=o2d(list1)
        h=h2d(list1)
    elif(choice.get()==3):
        b=d2b(h2d(list1))
        o=d2o(h2d(list1))
        d=h2d(list1)
    elif(choice.get()==4):
        b=b2g(list1)
    
    if(choice.get()!=0 and result[0].get()):
        binary=Label(Result, text="Binary", bg="#ffffbe")
        binary.grid(row=0,column=0, padx=5,pady=5, sticky=W)
        Binary=Entry(Result, width=30)
        Binary.grid(row=0,column=1,pady=5)
        Binary.insert(0, b)
        
    if(choice.get()!=1 and result[1].get()):
        octal=Label(Result, text="Octal", bg="#ffffbe")
        octal.grid(row=1,column=0, padx=5,pady=5, sticky=W)
        Octal=Entry(Result, width=30)
        Octal.grid(row=1,column=1,pady=5)
        Octal.insert(0, o)
        
    if(choice.get()!=2 and result[2].get()):
        decimal=Label(Result, text="Decimal", bg="#ffffbe")
        decimal.grid(row=2,column=0, padx=5,pady=5, sticky=W)
        Decimal=Entry(Result, width=30)
        Decimal.grid(row=2,column=1,pady=5)
        Decimal.insert(0, d)
        
    if(choice.get()!=3 and result[3].get()):
        hexadecimal=Label(Result, text="Hexadecimal", bg="#ffffbe")
        hexadecimal.grid(row=3,column=0, padx=5,pady=5, sticky=W)
        Hexadecimal=Entry(Result, width=30)
        Hexadecimal.grid(row=3,column=1,pady=5)
        Hexadecimal.insert(0, h)

    if(choice.get()!=4 and result[4].get()):
        graycode=Label(Result, text="Gray Code", bg="#ffffbe")
        graycode.grid(row=3,column=0, padx=5,pady=5, sticky=W)
        GrayCode=Entry(Result, width=30)
        GrayCode.grid(row=3,column=1,pady=5)
        GrayCode.insert(0, g)

    if all(i==0 for i in(result[0].get(), result[1].get(), result[2].get(), result[3].get(), result[4].get())):
        empty=Label(Result, text="No Output was chosen", bg="#ffffbe")
        empty.grid(row=4,column=0, padx=5,pady=5)

    rb1.config(state=NORMAL)
    rb2.config(state=NORMAL)
    rb3.config(state=NORMAL)
    rb4.config(state=NORMAL)

    
def start():
    global Number
    global rb1
    global rb2
    global rb3
    global rb4
    global rb5
    global cb1
    global cb2
    global cb3
    global cb4
    global cb5
    global Input
    
    frame.forget()
    root.config(bg="#ffffbe")
    title=Label(root, text="B.O.D.H.A.G. CONVERTER", font=("Calibri",20, "bold"), bg="#ffffbe")
    title.grid(row=0,column=0, pady=5, columnspan=2, stick=W+E)

    Input_text=LabelFrame(root, text="User Input", bg="#ffffbe", font=("Calibri",12), bd=3)
    Input_text.grid(row=1,column=0, padx=15, ipadx=5, ipady =5, columnspan=2, stick=W+E)
    
    Number=Entry(Input_text, width=40)
    Number.pack(padx=25, pady=5)

    Check=Button(root, text="Detect Number System", command=check, bg="#e5ecff", cursor="hand2", relief="groove")
    Check.grid(row=2,column=0, padx=5, pady=(10,0), ipadx=75, ipady =5, columnspan=2)
    
    Input=LabelFrame(root, text="Input", bg="#ffffbe", font=("Calibri",12))
    Input.grid(row=3,column=0, padx=5, pady=(10,0), ipadx=5, ipady =5)

    rb1=Radiobutton(Input, text="Binary", variable=choice, value=0, command=disable, bg="#ffffbe", activebackground="#ffff99", cursor="target")
    rb1.pack(anchor=W)
    rb2=Radiobutton(Input, text="Octal", variable=choice, value=1, command=disable, bg="#ffffbe", activebackground="#ffff99", cursor="target")
    rb2.pack(anchor=W)
    rb3=Radiobutton(Input, text="Decimal", variable=choice, value=2, command=disable, bg="#ffffbe", activebackground="#ffff99", cursor="target")
    rb3.pack(anchor=W)
    rb4=Radiobutton(Input, text="Hexadecimal", variable=choice, value=3, command=disable, bg="#ffffbe", activebackground="#ffff99", cursor="target")
    rb4.pack(anchor=W)
    rb5=Radiobutton(Input, text="Gray Code", variable=choice, value=4, command=disable, bg="#ffffbe", activebackground="#ffff99", cursor="target")
    rb5.pack(anchor=W)
              
    Output=LabelFrame(root, text="Output", bg="#ffffbe", font=("Calibri",12))
    Output.grid(row=3,column=1, padx=5, pady=(10,0), ipadx=5, ipady =5)   

    cb1=Checkbutton(Output, text="Binary", variable=result[0], onvalue=1, offvalue=0, state=DISABLED, bg="#ffffbe", activebackground="#ffff99", cursor="dotbox")
    cb1.pack(anchor=W)
    cb2=Checkbutton(Output, text="Octal", variable=result[1], onvalue=1, offvalue=0, bg="#ffffbe", activebackground="#ffff99", cursor="dotbox")
    cb2.pack(anchor=W)
    cb3=Checkbutton(Output, text="Decimal", variable=result[2], onvalue=1, offvalue=0, bg="#ffffbe", activebackground="#ffff99", cursor="dotbox")
    cb3.pack(anchor=W)
    cb4=Checkbutton(Output, text="Hexadecimal", variable=result[3], onvalue=1, offvalue=0, bg="#ffffbe", activebackground="#ffff99", cursor="dotbox")
    cb4.pack(anchor=W)
    cb5=Checkbutton(Output, text="Gray Code", variable=result[4], onvalue=1, offvalue=0, bg="#ffffbe", activebackground="#ffff99", cursor="dotbox")
    cb5.pack(anchor=W)

    Convert=Button(root, text="Convert", command=convert, bg="#e5ecff", cursor="hand2", relief="groove")
    Convert.grid(row=4,column=0, padx=5, pady=(10,15), ipadx=60, ipady =5, columnspan=2)    

    
frame=LabelFrame(root, text="GURYANSH SINGLA", padx=5, pady=5)
frame.pack(padx=10,pady=10)

title=Label(frame, text="B.O.D.H.A.G.", font=("BatmanForeverAlternate",40), fg="#002B5B")
title.pack()

subtitle=Label(frame, text="Binary Octal Decimal Hexadeciaml and Gray Code Converter")
subtitle.pack()

b=Button(frame, text="Start", command=start, cursor="hand2", relief="ridge", bd=2, bg="#F6F1E9")
b.pack(padx=10,pady=10, ipadx=20)


root.mainloop()
