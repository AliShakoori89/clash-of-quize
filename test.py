import tkinter as tk
from tkinter.ttk import *
from tkinter import *
import Json
from functools import partial
import time
from multiprocessing import Process
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
        self.option=self.json_obj.search_option(self.all_question[i])

        self.progress=Progressbar(self.root,orient=HORIZONTAL,length=100,mode='determinate', variable=self.barVar)
        self.progress.place(x=450,y=120)
        
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

        global t1
        global t2
        t1=Thread(target = self.respite_time)
        t1.start()
        t2=Thread(target = self.bar)
        t2.start()


    def respite_time(self):
        self.time_solve=self.root.after(10000,self.new_question)
        

    def bar(self): 
        self.progress['value'] = 10
        self.root.update_idletasks()
        self.barVar.set(10) 
        time.sleep(1) 

        self.progress['value'] = 20
        self.root.update_idletasks()
        self.barVar.set(20) 
        time.sleep(1) 

        self.progress['value'] = 30
        self.root.update_idletasks() 
        self.barVar.set(30)
        time.sleep(1) 

        self.progress['value'] = 40
        self.root.update_idletasks() 
        self.barVar.set(40)
        time.sleep(1) 

        self.progress['value'] = 50
        self.root.update_idletasks() 
        self.barVar.set(50)
        time.sleep(1) 

        self.progress['value'] = 60
        self.root.update_idletasks() 
        self.barVar.set(60)
        time.sleep(1) 

        self.progress['value'] = 70
        self.root.update_idletasks() 
        self.barVar.set(70)
        time.sleep(1) 

        self.progress['value'] = 80
        self.root.update_idletasks() 
        self.barVar.set(80)
        time.sleep(1) 

        self.progress['value'] = 90
        self.root.update_idletasks() 
        self.barVar.set(90)
        time.sleep(1) 
        self.progress['value'] = 100
        


    def read_question(self):
        question=self.json_obj.read_dictionary_keys()
        return question

    # def run(self): 
    #     while True: 
    #         # print('thread running') 
    #         global stop_threads 
    #         if stop_threads: 
    #             break

    def check_option(self,option,question):
        global points
        global t1
        your_select=option
        score=self.json_obj.check_answer(question,your_select)
        points+=score
        score_label_value=Label(self.root,text=points,font='Bnazanin 10 bold')
        score_label_value.place(x=70,y=120)
        self.root.after_cancel(self.time_solve)
        self.progress.destroy()
        self.progress=Progressbar(self.root,orient=HORIZONTAL,length=100,mode='determinate', variable=self.barVar)
        self.progress.place(x=450,y=120)
        self.root.after_cancel(self.bar)
        # global stop_threads
        # stop_threads = True
        # self.bar.wait()
        # self.root.update_idletasks() 
        # self.progress['value'] = 100
        # self.progress.destroy()
        # self.bar.
        # x = self.barVar.get()
        # if x < 100:
        #     x=0
        #     self.barVar.set(x+10)
        #     self.progress.stop()
        # self.update_progress_bar()
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


    # def update_progress_bar(self):
    #     x = self.barVar.get()
    #     if x < 100:
    #         x=0
    #         self.barVar.set(x+10)
    #         self.progress['value'] = 100
    #         # self.bar()


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

            # self.progress=Progressbar(self.root,orient=HORIZONTAL,length=100,mode='determinate', variable=self.barVar)
            # self.progress.place(x=450,y=120)

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

            Thread(target = self.respite_time).start()
            Thread(target = self.bar).start()
        else:
            self.root.destroy()
            self.points_label()
           
obj=Testpage()
obj.root.mainloop()