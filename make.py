import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
import Json
from functools import partial


class MainGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x320')
        self.root.title('Creat Test')
        self.json_obj=Json.JsonHandler()

        lable_for_write_test_question=Label(self.root,text=" : سوال ")
        lable_for_write_test_question.place(x=450, y=10)

        question_entry=Entry(self.root, bg='white', width=75, bd=2, selectborderwidth=5)
        question_entry.place(x=20,y=35)

        the_first_option=Label(self.root,text=" :گزینه اول ")
        the_first_option.place(x=430, y=80)

        the_first_option_entry=Entry(self.root, bg='white', width=40, bd=2, selectborderwidth=5)
        the_first_option_entry.place(x=230, y=100)

        the_second_option=Label(self.root,text=" :گزینه دوم ")
        the_second_option.place(x=430, y=130)

        the_second_option_entry=Entry(self.root, bg='white', width=40, bd=2, selectborderwidth=5)
        the_second_option_entry.place(x=230, y=150)

        the_third_option=Label(self.root,text=" :گزینه سوم ")
        the_third_option.place(x=430, y=180)

        the_third_option_entry=Entry(self.root, bg='white', width=40, bd=2, selectborderwidth=5)
        the_third_option_entry.place(x=230, y=200)

        the_option_four=Label(self.root,text=" :گزینه چهارم ")
        the_option_four.place(x=430, y=230)

        the_option_four_entry=Entry(self.root, bg='white', width=40, bd=2, selectborderwidth=5)
        the_option_four_entry.place(x=230, y=250)

        store_question_and_option=partial(self.add_question_option,question_entry,the_first_option_entry,\
                            the_second_option_entry,the_third_option_entry,\
                                the_option_four_entry)
        store_button=Button(self.root,text='Store Test' ,command=store_question_and_option,bd=4 ,width=20 ,activebackground='lightgrey' ,font='Bnazanin 10 bold')
        store_button.place(x=150,y=285)

        CheckVar1 = IntVar(self.root)
        CheckVar2 = IntVar(self.root)
        CheckVar3 = IntVar(self.root)
        CheckVar4 = IntVar(self.root)

        chechbox_label=Label(self.root,text='گزینه صحیح')
        chechbox_label.place(x=30,y=80)

        the_first_option_checkbox = Checkbutton(self.root, variable = CheckVar1, \
                 onvalue = 1, offvalue = 0 )
        the_first_option_checkbox.place(x=50,y=105)


        the_second_option_checkbox = Checkbutton(self.root, variable = CheckVar2, \
                 onvalue = 1, offvalue = 0 )
        the_second_option_checkbox.place(x=50,y=150)
        

        the_third_option_checkbox = Checkbutton(self.root, variable = CheckVar3, \
                 onvalue = 1, offvalue = 0)
        the_third_option_checkbox.place(x=50,y=200)


        the_optin_four_checkbox = Checkbutton(self.root, variable = CheckVar4, \
                 onvalue = 1, offvalue = 0)        
        the_optin_four_checkbox.place(x=50,y=250)

    def add_question_option(self,question_entry,the_first_option_entry,\
                            the_second_option_entry,the_third_option_entry,\
                                the_option_four_entry):
        question_entry=question_entry.get()
        the_first_option_entry=the_first_option_entry.get()
        the_second_option_entry=the_second_option_entry.get()
        the_third_option_entry=the_third_option_entry.get()
        the_option_four_entry=the_option_four_entry.get()

        dictionary={question_entry:{'1st':the_first_option_entry,"2st":the_second_option_entry,"3st":the_third_option_entry,"4st":the_option_four_entry}}
        print(dictionary)
        self.json_obj.add_dectionary(dictionary)
        



main=MainGUI()
main.root.mainloop()