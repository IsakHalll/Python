import os

os.system('cls')
"""
x=input("")

for i in range(10):
    print(x)
"""
"""
y=1
while True:
    print(y)
    if y == 10:
        break
    y += 1


x2=int(input("hur många: "))
y2=1
while True:
    print(y2)
    if y2 == x2:
        break
    y2 += 1
"""

for table in range(1, 13):
    print(f"TABELL{table}")
    for y in range (1, 11):
        print(f"{table} * {y} = {str(table *y)}")