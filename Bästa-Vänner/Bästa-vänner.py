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
friend_amount = len(my_list)


def list_name():
    for name in my_list:
        print(name)


def add_name(new):
    my_list.append(new)


def remove_name(remove):
    my_list.pop(remove)


def edit_name(edit, name):
    my_list[edit-1] = name


while True:
    print("A: Add" , "R: Remove", "E: Edit", "Q: Quit")
    keys = getwch().lower()
    
    os.system('cls')
    
    if keys == "a":
        new = input("Nytt namn: ")
        add_name(new)
        list_name()

    elif keys == "r":
        remove = int(input("Ta bort namn: "))
        remove_name(remove-1)
        list_name()

    elif keys == "e":
        edit = int(input("Vilket namn vill du ändra?" ))
        name = str(input("Skriv det nya namnet: "))
        edit_name(edit,name)
        list_name()

    elif keys == "q":
        print("Antal vänner: ", friend_amount)
        break