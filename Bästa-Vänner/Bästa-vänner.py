'''
Bästa-vänner.PY: Bästa vän lista

__author__  = "Isak Åkerberg"
__version__ = "1.0.0"
__email__   = "Isak.akerberg@elev.ga.ntig.se"
'''

import os
from msvcrt import getwch

my_list = ["nicklas",  "njclkas", "nicklad", "leonard"]
keys = ["A" , "R", "E", "Q"]
Friend_amount = len(my_list)


def list_name():
    return my_list

def add_name(new):
    my_list.append(new)

def remove_name(remove):
    my_list.pop(remove)

def edit_name(edit,name):
    my_list[edit-1] = name

while True:
    keys = getwch().lower()
    if keys == "a":
        new = input ("Nytt namn: ")
        add_name(new)
        print (list_name())
    elif keys == "r":
        remove = int(input("Ta bort namn: "))
        remove_name(remove-1)
        print(list_name())
    elif keys == "e":
        edit = int(input("Vilket namn vill du ändra?" ))
        name = str(input("Skriv det nya namnet: "))
        edit_name(edit,name)
        print(list_name())
    elif keys == "q":
        print("Antal vänner =", Friend_amount)
        break