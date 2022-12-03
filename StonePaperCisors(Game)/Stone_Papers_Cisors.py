#Stone papers and cisors game by Akarshan Rasyal

import random
from playsound import playsound

def game(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'p':
            return True
        elif you == 'c':
            return False
    elif comp == 'p':
        if you == 'c':
            return True
        elif you == 's':
            return False
    elif comp == 'c':
        if you == 's':
            return True
        elif you == 'p':
            return False

randNO = random.randint(1, 3)

if randNO == 1:
    comp = 's'
elif randNO == 2:
    comp = 'p'
elif randNO == 3:
    comp = 'c'

you = input("Choose one of the follwoing :\n\tStone(s) Papers(p) or Cisors(c)? : ")
a = game(comp, you)

if comp == 's':
    print("Computer chose Stone")
elif comp == 'p':
    print("Computer chose Papers")
elif comp == 'c':
    print("Computer chose Cisors")

if you == 's':
    print("You chose Stone")
elif you == 'p':
    print("You chose Papers")
elif you == 'c':
    print("You chose Cisors")

print(" ")    # To print a line between result and computers choice

if a == None:
    print("The game is a tie!")
    playsound('E:\\PROGRAMMING\\Pyhton\\Python\\GAME\\Sounds\\Its a tie.mp3')
elif a:
    print("You win!")
    playsound('E:\\PROGRAMMING\\Pyhton\\Python\\GAME\\Sounds\\You win.mp3')
else:
    print("You loose!")
    playsound('E:\\PROGRAMMING\\Pyhton\\Python\\GAME\\Sounds\\You loose.mp3')