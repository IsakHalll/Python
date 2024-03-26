import os
import json

os.system("cls")

text = input("Skriv något: ")

with open("test.json", "w") as my_file:
    json.dump(text, my_file)


with open("test.json", "r") as my_file:
    print(json.load(my_file))