from colors import bcolors
import random
import os
os.system('cls')

print (bcolors.BLUE + '''
-----================-----
  gissa talet från 1-100 
-----du har 7 försök!-----
''')


while True: 
    secret_number=random.randint(1,100)
    lives=7

    while True:    #Spelomgången startar
        try:
            guess=int(input(bcolors.DEFAULT + "Din gissning: "))
        except:
            print ("Skriv i heltal")
            continue

        if guess == secret_number:
            print(bcolors.GREEN + "Du gissade rätt")
            break
           
        elif guess > secret_number:
            print (bcolors.RED + bcolors.UNDERLINE + bcolors.BOLD + "GISSA LÄGRE!")
            lives-=1
            print (bcolors.DEFAULT + "Du har",lives,"försök kvar")
        elif guess < secret_number:
            print (bcolors.RED + bcolors.UNDERLINE + bcolors.BOLD + "GISSA HÖGRE!")
            lives-=1
            print (bcolors.DEFAULT + "Du har",lives,"försök kvar")
        if lives == 0:
            print(bcolors.RED + "Du förlorade")
            break

    again=input("Vill du spela igen? [j]=Ja [n]=Nej: ")
    if again.lower() == "n":
        exit()
    elif again.lower() == "j":
       continue            

