from tkinter import *

score = {}
def IT():
    def first_quiz():
        first = Tk()
        first.geometry('600x400')
        first.title('Quiz app')
        first.resizable(width=False, height=False)
        def next1_func():
            global score
            score['1'] = var.get()
            first.destroy()
            second_quiz()
        label_top = Label(first, bg='green', width=90, height=2, fg='white',text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
        label_top.pack()
        var = StringVar()
        var.set(0)
        quiz1 = Label(first, text='Hamma harfni kattalawtiribyoziladigan funksiya nima?',font=('Arial', 15, 'bold'))
        quiz1.place(x=70, y=100)
        radio1 = Radiobutton(first, text='upper()', value="Tog'ri", variable=var, font=('Arial', 15, 'normal'))
        radio1.place(x=70, y=140)
        radio2 = Radiobutton(first, text='lower()', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
        radio2.place(x=70, y=180)
        radio3 = Radiobutton(first, text='capitalize()', value="False", variable=var, font=('Arial', 15, 'normal'))
        radio3.place(x=70, y=220)
        radio4 = Radiobutton(first, text='print()', value="Error", variable=var, font=('Arial', 15, 'normal'))
        radio4.place(x=70, y=260)
        next = Button(first, text='Next', bg='blue', fg='white', width=13, height=2, command=next1_func)
        next.place(x=260, y=330)
        first.mainloop()
        
    def second_quiz():
        second = Tk()
        second.geometry('600x400')
        second.title('Quiz app')
        second.resizable(width=False, height=False)
        def next2_func():
            global score
            score['2'] = var.get()
            second.destroy()
            third_quiz()
        labell_top = Label(second, bg='green', width=90, height=2, fg='white',text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
        labell_top.pack()
        var = StringVar()
        var.set(0)
        quizz1 = Label(second, text='Quydagilardan float qiymatdagi sonlarni toping?',font=('Arial', 15, 'bold'))
        quizz1.place(x=70, y=100)
        radioo1 = Radiobutton(second, text='6876.0', value="False", variable=var, font=('Arial', 15, 'normal'))
        radioo1.place(x=70, y=140)
        radioo2 = Radiobutton(second, text='3578', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo2.place(x=70, y=180)
        radioo3 = Radiobutton(second, text='3.14', value="Error", variable=var, font=('Arial', 15, 'normal'))
        radioo3.place(x=70, y=220)
        radioo4 = Radiobutton(second, text='A va C javoblar togri', value="Tog'ri", variable=var, font=(
    'Arial', 15, 'normal'))
        radioo4.place(x=70, y=260)
        nextt = Button(second, text='Next', bg='blue', fg='white', width=13, height=2, command=next2_func)
        nextt.place(x=260, y=330)
        second.mainloop()
    def third_quiz():
        third = Tk()
        third.geometry('600x400')
        third.title('Quiz app')
        third.resizable(width=False, height=False)
        def next3_func():
            global score
            score['2'] = var.get()
            third.destroy()
            fourth_quiz()
        labell_top = Label(third, bg='green', width=90, height=2, fg='white',text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
        labell_top.pack()
        var = StringVar()
        var.set(0)
        quizz1 = Label(third, text='else , elif , if shu shartlardan foydalanishimiz uchun. Uning ketma ketligini topib bering?',font=('Arial', 15, 'bold'))
        quizz1.place(x=70, y=100)
        radioo1 = Radiobutton(third, text='elif , if , else', value="False", variable=var, font=('Arial', 15, 'normal'))
        radioo1.place(x=70, y=140)
        radioo2 = Radiobutton(third, text='if , else , elif', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo2.place(x=70, y=180)
        radioo3 = Radiobutton(third, text='else , elif , if', value="Error", variable=var, font=('Arial', 15,'normal', ))
        radioo3.place(x=70, y=220)
        radioo4 = Radiobutton(third, text='if , elif, else', value="Tog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo4.place(x=70, y=260)
        nextt = Button(third, text='Next', bg='blue', fg='white', width=13, height=2, command=next3_func)
        nextt.place(x=260, y=330)
        third.mainloop()
    def fourth_quiz():
        fourth = Tk()
        fourth.geometry('600x400')
        fourth.title('Quiz app')
        fourth.resizable(width=False, height=False)
        def next4_func():
            global score
            score['4'] = var.get()
            fourth.destroy()
            fiveth_quiz()
        labell_top = Label(fourth, bg='green', width=90, height=2, fg='white',
            text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
        labell_top.pack()
        var = StringVar()
        var.set(0)
        quizz1 = Label(fourth, text='Listga malumot qoshish?',font=('Arial', 15, 'bold'))
        quizz1.place(x=70, y=100)
        radioo1 = Radiobutton(fourth, text='remove()', value="False", variable=var, font=('Arial', 15, 'normal'))
        radioo1.place(x=70, y=140)
        radioo2 = Radiobutton(fourth, text='[]', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo2.place(x=70, y=180)
        radioo3 = Radiobutton(fourth, text='append()', value="Tog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo3.place(x=70, y=220)
        radioo4 = Radiobutton(fourth, text='2 va 3 chi tori', value="Error", variable=var, font=('Arial', 15, 'normal'))
        radioo4.place(x=70, y=260)
        nextt = Button(fourth, text='Next', bg='blue', fg='white', width=13, height=2, command=next4_func)
        nextt.place(x=260, y=330)
        fourth.mainloop()
    def fiveth_quiz():
        fiveth = Tk()
        fiveth.geometry('600x400')
        fiveth.title('Quiz app')
        fiveth.resizable(width=False, height=False)
        def next5_func():
            global score
            score['5'] = var.get()
            fiveth.destroy()
            sixth_quiz()
        labell_top = Label(fiveth, bg='green', width=90, height=2, fg='white',text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
        labell_top.pack()
        var = StringVar()
        var.set(0)
        quizz1 = Label(fiveth, text='Listdan malumot ochirish?',font=('Arial', 15, 'bold'))
        quizz1.place(x=70, y=100)
        radioo1 = Radiobutton(fiveth, text='remove()', value="Tog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo1.place(x=70, y=140)
        radioo2 = Radiobutton(fiveth, text='[]', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo2.place(x=70, y=180)
        radioo3 = Radiobutton(fiveth, text='append()', value="False", variable=var, font=('Arial', 15, 'normal'))
        radioo3.place(x=70, y=220)
        radioo4 = Radiobutton(fiveth, text='2 va 3 chi tori', value="Error", variable=var, font=('Arial', 15, 'normal'))
        radioo4.place(x=70, y=260)
        nextt = Button(fiveth, text='Next', bg='blue', fg='white', width=13, height=2, command=next5_func)
        nextt.place(x=260, y=330)
        fiveth.mainloop()
    def sixth_quiz():
        sixth = Tk()
        sixth.geometry('600x400')
        sixth.title('Quiz app')
        sixth.resizable(width=False, height=False)
        def next6_func():
            global score
            score['6'] = var.get()
            sixth.destroy()
            seventh_quiz()
        labell_top = Label(sixth, bg='green', width=90, height=2, fg='white', text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
        labell_top.pack()
        var = StringVar()
        var.set(0)
        quizz1 = Label(sixth, text='fg nima qiladi?',font=('Arial', 15, 'bold'))
        quizz1.place(x=70, y=100)
        radioo1 = Radiobutton(sixth, text='oynaning rangini ozgartiradi', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo1.place(x=70, y=140)
        radioo2 = Radiobutton(sixth, text='yozuvni rangini ozgartiradi', value="Tog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo2.place(x=70, y=180)
        radioo3 = Radiobutton(sixth, text='ekranga obzats beradi', value="False", variable=var, font=('Arial', 15, 'normal'))
        radioo3.place(x=70, y=220)
        radioo4 = Radiobutton(sixth, text='hammasi togri', value="Error", variable=var, font=('Arial', 15, 'normal'))
        radioo4.place(x=70, y=260)
        nextt = Button(sixth, text='Next', bg='blue', fg='white', width=13, height=2, command=next6_func)
        nextt.place(x=260, y=330)
        sixth.mainloop()
    def seventh_quiz():
        seventh = Tk()
        seventh.geometry('600x400')
        seventh.title('Quiz app')
        seventh.resizable(width=False, height=False)
        def next7_func():
            global score
            score['7'] = var.get()
            seventh.destroy()
            eightth_quiz()
        labell_top = Label(seventh, bg='green', width=90, height=2, fg='white',text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
        labell_top.pack()
        var = StringVar()
        var.set(0)
        quizz1 = Label(seventh, text='Sarlavha beradigan funksiya?',font=('Arial', 15, 'bold'))
        quizz1.place(x=70, y=100)
        radioo1 = Radiobutton(seventh, text='geometry', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo1.place(x=70, y=140)
        radioo2 = Radiobutton(seventh, text='resizable', value="Error", variable=var, font=('Arial', 15, 'normal'))
        radioo2.place(x=70, y=180)
        radioo3 = Radiobutton(seventh, text='Tk()', value="False", variable=var, font=('Arial', 15, 'normal'))
        radioo3.place(x=70, y=220)
        radioo4 = Radiobutton(seventh, text='title', value="Tog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo4.place(x=70, y=260)
        nextt = Button(seventh, text='Next', bg='blue', fg='white', width=13, height=2, command=next7_func)
        nextt.place(x=260, y=330)
        seventh.mainloop() 
    def eightth_quiz():
        eightth = Tk()
        eightth.geometry('600x400')
        eightth.title('Quiz app')
        eightth.resizable(width=False, height=False)
        def next8_func():
            global score
            score['8'] = var.get()
            eightth.destroy()
            nineth_quiz()
        labell_top = Label(eightth, bg='green', width=90, height=2, fg='white', text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
        labell_top.pack()
        var = StringVar()
        var.set(0)
        quizz1 = Label(eightth, text='Celsiy formulasi?',font=('Arial', 15, 'bold'))
        quizz1.place(x=70, y=100)
        radioo1 = Radiobutton(eightth, text='5/9(150+32)', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo1.place(x=70, y=140)
        radioo2 = Radiobutton(eightth, text='9/5(150+32)', value="Error", variable=var, font=('Arial', 15, 'normal'))
        radioo2.place(x=70, y=180)
        radioo3 = Radiobutton(eightth, text='5*9(150-32)', value="False", variable=var, font=('Arial', 15, 'normal'))
        radioo3.place(x=70, y=220)
        radioo4 = Radiobutton(eightth, text='5/9*(150-32)', value="Tog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo4.place(x=70, y=260)
        nextt = Button(eightth, text='Next', bg='blue', fg='white', width=13, height=2, command=next8_func)
        nextt.place(x=260, y=330)
        eightth.mainloop()
    def nineth_quiz():
        nineth = Tk()
        nineth.geometry('600x400')
        nineth.title('Quiz app')
        nineth.resizable(width=False, height=False)
        def next9_func():
            global score
            score['9'] = var.get()
            nineth.destroy()
            tenth_quiz()
        labell_top = Label(nineth, bg='green', width=90, height=2, fg='white',text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
        labell_top.pack()
        var = StringVar()
        var.set(0)
        quizz1 = Label(nineth, text='Texnologiya bu nima?',font=('Arial', 15, 'bold'))
        quizz1.place(x=70, y=100)
        radioo1 = Radiobutton(nineth, text='yangi narsalar', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo1.place(x=70, y=140)
        radioo2 = Radiobutton(nineth, text='tosh', value="Tog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo2.place(x=70, y=180)
        radioo3 = Radiobutton(nineth, text='computer', value="False", variable=var, font=('Arial', 15, 'normal'))
        radioo3.place(x=70, y=220)
        radioo4 = Radiobutton(nineth, text='noutbuk', value="Error", variable=var, font=('Arial', 15, 'normal'))
        radioo4.place(x=70, y=260)
        nextt = Button(nineth, text='Next', bg='blue', fg='white', width=13, height=2, command=next9_func)
        nextt.place(x=260, y=330)
        nineth.mainloop()
    def tenth_quiz():
        tenth = Tk()
        tenth.geometry('600x400')
        tenth.title('Quiz app')
        tenth.resizable(width=False, height=False)
        def next10_func():
            global score
            score['10'] = var.get()
            print(score)
            tenth.destroy()
                   
        labell_top = Label(tenth, bg='green', width=90, height=2, fg='white',text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
        labell_top.pack()
        var = StringVar()
        var.set(0)
        quizz1 = Label(tenth, text='font() ga nechta argument bersa boladi?',font=('Arial', 15, 'bold'))
        quizz1.place(x=70, y=100)
        radioo1 = Radiobutton(tenth, text='3', value="Tog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo1.place(x=70, y=140)
        radioo2 = Radiobutton(tenth, text='2', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo2.place(x=70, y=180)
        radioo3 = Radiobutton(tenth, text='4', value="False", variable=var, font=('Arial', 15, 'normal'))
        radioo3.place(x=70, y=220)
        radioo4 = Radiobutton(tenth, text='5', value="Error", variable=var, font=('Arial', 15, 'normal'))
        radioo4.place(x=70, y=260)
        nextt = Button(tenth, text='Next', bg='blue', fg='white', width=13, height=2, command=next10_func)
        nextt.place(x=260, y=330)
        tenth.mainloop()
        
    first_quiz()
