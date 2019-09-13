import tkinter as tk
from tkinter.ttk import *
from tkinter import *
import Json
from functools import partial
import time
from threading import Thread
from progressbar import ProgressBar
import threading
# import ttk
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
        self.first_question_label=Label(self.root,text=self.all_question[i])
        self.first_question_label.pack( side = TOP  )
        self.barVar = DoubleVar()
        self.barVar.set(0)
        self.max=200
        self.option=self.json_obj.search_option(self.all_question[i])

        self.progbar1=Progressbar(self.root,orient=HORIZONTAL,length=100,mode='determinate', variable=self.barVar,maximum=self.max)
        self.progbar1.place(x=450,y=120)
        
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
        
        self.score_label=Label(self.root,text='score:',font='Bnazanin 10 bold')
        self.score_label.place(x=30,y=120)
        self.progbar1.start()
        self.time_solve=self.root.after(10000,self.new_question)
        


    def read_question(self):
        question=self.json_obj.read_dictionary_keys()
        return question

    def check_option(self,option,question):
        global points
        # global t1
        your_select=option
        score=self.json_obj.check_answer(question,your_select)
        points+=score
        score_label_value=Label(self.root,text=points,font='Bnazanin 10 bold')
        score_label_value.place(x=70,y=120)
        self.root.after_cancel(self.time_solve)
        self.progbar1.destroy()
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

    def add_progbar(self):
        self.progbar=Progressbar(self.root,orient=HORIZONTAL,length=100,mode='determinate', variable=self.barVar,maximum=self.max)
        self.progbar.place(x=450,y=120)

    def new_question(self):
        global i
        i+=1
        question=self.read_question()
        n=len(question)
        
        if i>1:
            self.question_label.destroy()
        if i!=n:
            self.all_question=self.read_question()
            self.first_question_label.destroy()
            self.question_label=Label(self.root,text=self.all_question[i])
            self.question_label.pack( side = TOP  )
            
            self.option=self.json_obj.search_option(self.all_question[i])
            self.add_progbar()
            

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
            
            self.score_label=Label(self.root,text='score:',font='Bnazanin 10 bold')
            self.score_label.place(x=30,y=120)

            for x in range(0, 200, 2):
                self.barVar.set(x)
                time.sleep(.1)
                self.root.update()
            self.progbar.destroy()

            
            self.time_solve=self.root.after(0,self.new_question)
            


        else:
            self.root.destroy()
            self.points_label()
           
obj=Testpage()
obj.root.mainloop()