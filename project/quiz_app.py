from tkinter import *
from It_page import IT,score
from MATH1_page import MATH,score1
from Logic_page import Logic,score2
import json
from PIL import Image,ImageTk
def register():
    registerr = Tk()
    registerr.geometry("300x450")
    registerr.title("Tkinter widgets ! ")
    registerr.config(bg='#34eb9b')
    registerr.resizable(0, 0)
    def ochir():
        if entr18.get() =="":
            label17["text"] = "Username kiriting"
            label17["fg"] ="red"
        elif entry1.get() =="":
            label2["text"] = "First Name kiriting"
            label2["fg"] ="red"

        elif entry4.get() =="":
            label3["text"] = "Last Name kiriting"
            label3["fg"] ="red"
        elif entry6.get() =="" :
            label5["text"] = "Phone Number kiriting"
            label5["fg"] ="red"

        elif entry8.get() =="" or "@" not in entry8.get():
            label7["text"] = "E-Mail kiriting"
            label7["fg"] ="red"

        elif entry10.get() =="":
            label9["text"] = "Password kiriting"
            label9["fg"] ="red"
        elif entry12.get() =="":
            label11["text"] = "Conf_password kiriting"
            label11["fg"] ="red"
        
        
        else:
            bio = {
                        "name":entr18.get(),
                        "first_name":entry1.get(),
                        "last_name":entry4.get(),
                        "phone_number":entry6.get(),
                        "email":entry8.get(),
                        "password":entry10.get(),
                        "Conf_password":entry12.get()
            
            }
            with open("quiz_app.json","w")as a:
                json.dump(bio,a)
        
            registerr.destroy()
            choose_page()
        
    label1 = Label(registerr, text="Registration", bg='#34eb9b', foreground='black', font=('Helvatica', 15, 'bold'))
    label1.pack()
    label17 = Label(registerr, text='Username', bg='#34eb9b', foreground='white', font=('Helvatica', 10, 'bold'))
    label17.pack(padx=10)
    entr18 = Entry(registerr)
    entr18.pack(padx=11)
    label2 = Label(registerr, text="First Name", bg='#34eb9b', foreground='white', font=('Helvatica', 10, 'bold'))
    label2.pack(padx=4)
    entry1 = Entry(registerr)
    entry1.pack(padx=5)
    label3 = Label(registerr, text="Last Name", bg='#34eb9b', foreground='white', font=('Helvatica', 10, 'bold'))
    label3.pack(padx=6)
    entry4 = Entry(registerr)
    entry4.pack(padx=7)
    label5 = Label(registerr, text="Phone Number", bg='#34eb9b', foreground='white', font=('Helvatica', 10, 'bold'))
    label5.pack(padx=8)
    entry6 = Entry(registerr)
    entry6.pack(padx=9)
    label7 = Label(registerr, text='E-Mail', bg='#34eb9b', foreground='white', font=('Helvatica', 10, 'bold'),)
    label7.pack(padx=10)
    entry8 = Entry(registerr)
    entry8.pack(padx=11)
    label9 = Label(registerr, text='Password', bg='#34eb9b', foreground='white', font=('Helvatica', 10, 'bold'))
    label9.pack(padx=10)
    entry10 = Entry(registerr, show='*')
    entry10.pack(padx=11)
    label11 = Label(registerr, text='Conf_password', bg='#34eb9b', foreground='white', font=('Helvatica', 10, 'bold'))
    label11.pack(padx=10)
    entry12 = Entry(registerr, show='*')
    entry12.pack(padx=11)
    a = StringVar()
    a.set(0)
    radio = Radiobutton(registerr, text='Male', bg='#34eb9b',
    value='Male', variable=a)
    radio.place(x=60, y=380)
    radi1 = Radiobutton(registerr, text='Famale',bg='#34eb9b',
    variable=a, value='Famale')
    radi1.place(x=150, y=380)
    btn = Button(registerr,text="Next",font=('Helvatica',15,'normal'), command=ochir)
    btn.place(x=130, y=410)
    
    registerr.mainloop()
    
def choose_page():
    win = Tk()

    def page():
        win.destroy()
        Logic()
    def page2():
        win.destroy()
        IT()
    def page3():
        win.destroy()
        MATH()
    button = Button(win, text='Logical', width=10, height=5,command=page)
    button.pack()
    butto2 = Button(win, text='IT', width=10, height=5,command=page2)
    butto2.pack()
    butto3 = Button(win, text='Math', width=10, height=5,command=page3)
    butto3.pack()
    win.mainloop()
    

def score_page():
    root = Tk()
    root.geometry("600x400")  


    frame1 = Frame(root,width= 300,height=500,bg="red")
    frame1.place(x= 0,y= 0)

    frame2 = Frame(root,width= 300,height=500,bg="green")
    frame2.place(x= 300,y= 0)
    f = Image.open('abc.jpg').resize((200,200))
    g = ImageTk.PhotoImage(f)
    h = Label(frame1,image=g)
    h.place(x=40,y=90)
    

    with open("quiz_app.json","r")as a:
         w =json.load(a)
    r =30
    for k,v in w.items():
        aa = Label(frame2,text=f"{k}: {v}",bg="green",fg="white")
        aa.place(x=25,y=r)
        r +=30
    togri_jovoblar =0
    notogri_jovoblar =0
    for k,v in score.items():
        if v== "Tog'ri":
           togri_jovoblar += 1
        else:
            notogri_jovoblar +=1 
    qq = Label(frame2,text=f"Togri javoblar:{togri_jovoblar}",bg="green",fg="white")
    qq.place(x=25,y=300)
    qq1 = Label(frame2,text=f"Notogri javoblar:{notogri_jovoblar}",bg="green",fg="white")
    qq1.place(x=25,y=350)
    if togri_jovoblar >=7:

        qq12 = Label(frame2,text=f"Imthon topwirdi ",bg="green",fg="white",font="bold")
        qq12.place(x=25,y=350)
    else:
        qq12 = Label(frame2,text=f"Imthon topwirilmadi ",bg="green",fg="red",font="bold")
        qq12.place(x=25,y=350)
    root.mainloop()


def score_page():
    root = Tk()
    root.geometry("600x400")  


    frame1 = Frame(root,width= 300,height=500,bg="red")
    frame1.place(x= 0,y= 0)

    frame2 = Frame(root,width= 300,height=500,bg="green")
    frame2.place(x= 300,y= 0)
    f = Image.open('abc.jpg').resize((200,200))
    g = ImageTk.PhotoImage(f)
    h = Label(frame1,image=g)
    h.place(x=40,y=90)
    

    with open("quiz_app.json","r")as a:
         w =json.load(a)
    r =30
    for k,v in w.items():
        aa = Label(frame2,text=f"{k}: {v}",bg="green",fg="white")
        aa.place(x=25,y=r)
        r +=30
    togri_jovoblar =0
    notogri_jovoblar =0
    for k,v in score1.items():
        if v== "Tog'ri":
           togri_jovoblar += 1
        else:
            notogri_jovoblar +=1 
    qq = Label(frame2,text=f"Togri javoblar:{togri_jovoblar}",bg="green",fg="white")
    qq.place(x=25,y=300)
    qq1 = Label(frame2,text=f"Notogri javoblar:{notogri_jovoblar}",bg="green",fg="white")
    qq1.place(x=25,y=350)
    if togri_jovoblar >=7:

        qq12 = Label(frame2,text=f"Imthon topwirdi ",bg="green",fg="white",font="bold")
        qq12.place(x=25,y=350)
    else:
        qq12 = Label(frame2,text=f"Imthon topwirilmadi ",bg="green",fg="red",font="bold")
        qq12.place(x=25,y=350)
    root.mainloop()



def score_page():
    root = Tk()
    root.geometry("600x400")  


    frame1 = Frame(root,width= 300,height=500,bg="red")
    frame1.place(x= 0,y= 0)

    frame2 = Frame(root,width= 300,height=500,bg="green")
    frame2.place(x= 300,y= 0)
    f = Image.open('abc.jpg').resize((200,200))
    g = ImageTk.PhotoImage(f)
    h = Label(frame1,image=g)
    h.place(x=40,y=90)
    

    with open("quiz_app.json","r")as a:
         w =json.load(a)
    r =30
    for k,v in w.items():
        aa = Label(frame2,text=f"{k}: {v}",bg="green",fg="white")
        aa.place(x=25,y=r)
        r +=30
    togri_jovoblar =0
    notogri_jovoblar =0
    for k,v in score2.items():
        if v== "Tog'ri":
           togri_jovoblar += 1
        else:
            notogri_jovoblar +=1 
    qq = Label(frame2,text=f"Togri javoblar:{togri_jovoblar}",bg="green",fg="white")
    qq.place(x=25,y=300)
    qq1 = Label(frame2,text=f"Notogri javoblar:{notogri_jovoblar}",bg="green",fg="white")
    qq1.place(x=25,y=350)
    if togri_jovoblar >=7:

        qq12 = Label(frame2,text=f"Imthon topwirdi ",bg="green",fg="white",font="bold")
        qq12.place(x=25,y=350)
    else:
        qq12 = Label(frame2,text=f"Imthon topwirilmadi ",bg="green",fg="red",font="bold")
        qq12.place(x=25,y=350)
    root.mainloop()

register()
score_page()

