import json
import os.path

class JsonHandler:
    
    def add_dectionary(self,dictionary):
        data={}
        if not os.path.isfile('dictionary.json'):
            with open('dictionary.json','w')as f:
                f.write(json.dumps(dictionary))
        else:
            with open('dictionary.json')as f:
                data=json.load(f)
            data.update(dictionary)
            with open('dictionary.json', 'w') as f:
                f.write(json.dumps(data)) 
    

    def read_dictionary_keys(self):
        question=[]
        with open('dictionary.json','r')as f:
            data=json.load(f)
            for key, value in data.items():
                question.append(key)
            return question

    def read_dictionary_values(self):
        values=[]
        with open('dictionary.json','r')as f:
            data=json.load(f)
            for key, value in data.items():
                for j in range(1,5):
                    j=str(j)
                    values.append(data[key][j])
                return values


    def check_answer(self,question,your_select):
        score=0
        with open('dictionary.json','r')as f:
            data=dict(json.load(f))
            if your_select!=data[question]['5']:
                return score
            else:
                score+=1
                return score

    
    def search_option(self,question):
        with open('dictionary.json','r')as f:
            data=json.load(f)
            for key, value in data.items():
                if question==key:
                    return value

