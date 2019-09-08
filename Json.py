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


        