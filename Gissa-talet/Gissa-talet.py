import random
import os
os.system('cls')

print ("---gissa talet från 1-100---")

secret_number=random.randint(1,100)
lives=7

while True:
    try:
        guess=int(input("Din gissning: "))
        if guess == secret_number:
            print("Du gissade rätt")
            break
        elif guess > secret_number:
            print ("lägre")
            lives-=1
            print ("Du har",lives,"försök kvar")
        elif guess < secret_number:
            print("högre")
            lives-=1
            print ("Du har",lives,"försök kvar")
        if lives == 0:
            print("Du förlorade")
            break
    except:
        print ("Skriv i heltal")

