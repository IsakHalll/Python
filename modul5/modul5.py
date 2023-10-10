import os
os.system('cls')
"""
names = ["isak", "viggo", "nicklas", "leonard", "leo"]
names[0]="albert"

for i in names:
    print(i)

print(len(names))

names.append("viktor")

for i in names:
    print(i)

print(len(names))

names.pop(1)

for i in names:
    print(i)


while True:
    names2 = []
   
    while True:
        for i in names2:
            print (i)

        name = input("Skriv namn här [1] = ta bort namn: ")

        if name == "1":
            remove_name = int(input("vilket namn vill du ta bort?: "))
            names2.pop(remove_name - 1)
           
        else:
            names2.append(name)
"""

carlib = {
    "Brand": "Toyota",
    "Model": "AE86 Sprinter Trueno",
    "year:": "1972"
}

print(carlib) 