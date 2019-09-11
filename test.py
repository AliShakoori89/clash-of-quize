import tkinter as tk
from tkinter import *
import Json
from functools import partial
# import make
global i
i=0
global points
points=0
class Testpage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('600x150')
        self.root.title('Question Page')
        self.json_obj=Json.JsonHandler()
        self.all_question=self.read_question()
        question_label=Label(self.root,text=self.all_question[i])
        question_label.pack( side = TOP  )

        self.option=self.json_obj.search_option(self.all_question[i])

        select_option_value=partial(self.check_option,self.option['1'],self.all_question[i])
        option_label=Button(self.root,text=self.option['1'],width=30,justify=RIGHT , command=select_option_value )
        option_label.place(x=350,y=40)
        
        select_option_value=partial(self.check_option,self.option['2'],self.all_question[i])
        option_label=Button(self.root,text=self.option['2'],width=30,justify=RIGHT , command=select_option_value )
        option_label.place(x=50,y=40)
        
        select_option_value=partial(self.check_option,self.option['3'],self.all_question[i])
        option_label=Button(self.root,text=self.option['3'],width=30,justify=RIGHT , command=select_option_value )
        option_label.place(x=350,y=80)

        select_option_value=partial(self.check_option,self.option['4'],self.all_question[i])
        option_label=Button(self.root,text=self.option['4'],width=30,justify=RIGHT , command=select_option_value )
        option_label.place(x=50,y=80)
        
        score_label=Label(self.root,text='score:',font='Bnazanin 10 bold')
        score_label.place(x=30,y=120)
        
        self.root.after(5000,self.new_question)

    def read_question(self):
        question=self.json_obj.read_dictionary_keys()
        return question


    def check_option(self,option,question):
        global points
        your_select=option
        score=self.json_obj.check_answer(question,your_select)
        points+=score
        score_label_value=Label(self.root,text=points,font='Bnazanin 10 bold')
        score_label_value.place(x=70,y=120)
        self.root.after_cancel(self.new_question)
        self.new_question()
        
    def points_label(self):
        global points
        self.root = tk.Tk()
        self.root.geometry('300x150')
        self.root.title('Point Page')
        points_label=Label(self.root,text="your points :",font='Bnazanin 20 bold')
        points_label.place(x=15,y=50)
        points_label=Label(self.root,text=points ,font='Bnazanin 20 bold')
        points_label.place(x=200,y=50)



    def new_question(self):
        global i
        i+=1
        question=self.read_question()
        n=len(question)
        if i!=n:
            self.all_question=self.read_question()
            question_label=Label(self.root,text=self.all_question[i])

            self.option=self.json_obj.search_option(self.all_question[i])

            select_option_value=partial(self.check_option,self.option['1'],self.all_question[i])
            option_label1=Button(self.root,text=self.option['1'],width=30,justify=RIGHT , command=select_option_value )
            
            select_option_value=partial(self.check_option,self.option['2'],self.all_question[i])
            option_label2=Button(self.root,text=self.option['2'],width=30,justify=RIGHT , command=select_option_value )
            
            select_option_value=partial(self.check_option,self.option['3'],self.all_question[i])
            option_label3=Button(self.root,text=self.option['3'],width=30,justify=RIGHT , command=select_option_value )

            select_option_value=partial(self.check_option,self.option['4'],self.all_question[i])
            option_label4=Button(self.root,text=self.option['4'],width=30,justify=RIGHT , command=select_option_value )

            
            score_label=Label(self.root,text='score:',font='Bnazanin 10 bold')
            
            self.new_question_window(question_label,option_label1,option_label2,option_label3,option_label4,score_label)
        else:
            self.root.destroy()
            self.points_label()

    def new_question_window(self,question_label,option_label1,option_label2,option_label3,option_label4,score_label):
        global i
        self.root.destroy()
        obj1=Testpage()
        obj1.root.mainloop()
            
           
obj=Testpage()
obj.root.mainloop(i)