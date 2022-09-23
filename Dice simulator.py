#Dice
import random
def Dice():
    n=random.randint(1,6)
    print("Rolling the dice.......")
    print(f"The number on the dice is: {n}")
Dice()
while(1):
        reply=input("Do you want to roll the dice again(S/NO)?")
        if reply=='S':
            Dice()
        else:
            print("Thanks for rolling me,I will be ready to roll whenver you need me.")
            break
   
