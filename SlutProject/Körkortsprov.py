import json
import os
from msvcrt import getwch

current_dir = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(current_dir, "KörkortsFrågor.json")
questions = None

with open(file_name, 'r', encoding='utf-8') as file:
    questions = json.load(file)

keys=["a","b","c","d"]

count=0

os.system('cls')

while True:
    
    while True:
        print(questions[count]["question"])
        for i in range(0,4):
            print(questions[count]["answers"][i])
        
        answer = getwch().lower()
            
        count +=1
        if answer in keys:  
            break

