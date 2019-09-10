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

        question_entry=Entry(self.root, bg='white', justify=RIGHT,width=75, bd=2, selectborderwidth=5)
        question_entry.place(x=20,y=35)

        the_first_option=Label(self.root,text=" :گزینه اول ")
        the_first_option.place(x=430, y=80)

        the_first_option_entry=Entry(self.root, bg='white',justify=RIGHT , width=40, bd=2, selectborderwidth=5)
        the_first_option_entry.place(x=230, y=100)

        the_second_option=Label(self.root,text=" :گزینه دوم ")
        the_second_option.place(x=430, y=130)

        the_second_option_entry=Entry(self.root, bg='white',justify=RIGHT , width=40, bd=2, selectborderwidth=5)
        the_second_option_entry.place(x=230, y=150)

        the_third_option=Label(self.root,text=" :گزینه سوم ")
        the_third_option.place(x=430, y=180)

        the_third_option_entry=Entry(self.root, bg='white',justify=RIGHT , width=40, bd=2, selectborderwidth=5)
        the_third_option_entry.place(x=230, y=200)

        the_option_four=Label(self.root,text=" :گزینه چهارم ")
        the_option_four.place(x=430, y=230)

        the_option_four_entry=Entry(self.root, bg='white',justify=RIGHT , width=40, bd=2, selectborderwidth=5)
        the_option_four_entry.place(x=230, y=250)

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


        store_question_and_option=partial(self.add_question_option,CheckVar1,CheckVar2,CheckVar3,CheckVar4,question_entry,the_first_option_entry,\
                            the_second_option_entry,the_third_option_entry,\
                                the_option_four_entry)

        store_button=Button(self.root,text='Store Question' ,command=store_question_and_option,bd=4 ,width=20 ,activebackground='lightgrey' ,font='Bnazanin 10 bold')
        store_button.place(x=50,y=285)

        store_button=Button(self.root,text='Next Questtion' ,command=self.rerun_app ,bd=4 ,width=20 ,activebackground='lightgrey' ,font='Bnazanin 10 bold')
        store_button.place(x=280,y=285)

        



    def check_true_option(self,CheckVar1,CheckVar2,CheckVar3,CheckVar4,the_first_option_entry,\
                                the_second_option_entry,the_third_option_entry,the_option_four_entry):
    
        if CheckVar1.get()==1:
            test_value=the_first_option_entry
            return test_value
        elif CheckVar2.get()==1:
            test_value=the_second_option_entry
            return test_value
        elif CheckVar3.get()==1:
            test_value=the_third_option_entry
            return test_value
        else:
            test_value=the_option_four_entry
            return test_value


    def add_question_option(self,CheckVar1,CheckVar2,CheckVar3,CheckVar4,question_entry,the_first_option_entry,\
                            the_second_option_entry,the_third_option_entry,\
                                the_option_four_entry):
        question_entry=question_entry.get()
        the_first_option_entry=the_first_option_entry.get()
        the_second_option_entry=the_second_option_entry.get()
        the_third_option_entry=the_third_option_entry.get()
        the_option_four_entry=the_option_four_entry.get()

        true_option=self.check_true_option(CheckVar1,CheckVar2,CheckVar3,CheckVar4,the_first_option_entry,\
                                the_second_option_entry,the_third_option_entry,the_option_four_entry)
                                
        dictionary={question_entry:{1:the_first_option_entry,2:the_second_option_entry,3:the_third_option_entry,4:the_option_four_entry,5:true_option,"question":question_entry}}
        print(dictionary)
        self.json_obj.add_dectionary(dictionary)

    def rerun_app(self):
        self.root.destroy()
        main=MainGUI()
        main.root.mainloop()

    
main=MainGUI()
main.root.mainloop()