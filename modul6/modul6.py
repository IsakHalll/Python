from msvcrt import getwch

import os
os.system ('cls')

"""
def calc_me(x, y):
    return x + y
print (calc_me(1, 1))


def my_name(x):
    return(x)
print (my_name("Isak"))


def calc_me2(x, y):
    return (x + y)

i=0
while i <= 10:
    print(calc_me2(1,2))
    i = i + 1
"""

my_list = ["nicklas",  "njclkas", "nicklad", "leonard"]
keys = ["A" , "R", "E"]

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


"""
def calc(x, y, op):
    if op == "+":
        return x+y
    elif op == "-":
        return x-y
    elif op == "*":
        return x*y
    elif op == "/":
        return x/y

op = input("ange räknesätt(+, -, *, /):")
x = float(input()) 
y = float(input()) 

result = calc(x, y, op)
print(result)
"""