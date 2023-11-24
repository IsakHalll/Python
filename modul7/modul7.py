import os, time
from colors import bcolors
from msvcrt import getwch
os.system('cls')
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
os.system('cls')
x = float(input()) 
os.system('cls')
y = float(input())
os.system('cls')
print("calculating...")

time.sleep(2)
os.system('cls')
result = calc(x, y, op)
print ("Svar:" , bcolors.GREEN + str(result))


keys = ["j","n"]

print("Välkommen\nskriv namn och ålder")
a = input("namn: ")
b = input("ålder: ")
print("är du en människa?\nJ=ja" , "N=nej")

keys = getwch().lower()
if keys == "j":
    print(a,b)
elif keys == "n":
    print("Du är inte välkommen")
"""