#Dice
import random
def Dice():
    dice_Number=random.randint(1,6)
    print("Rolling the dice.......")
    print(f"The number on the dice is: {dice_Number}")
Dice()
while(1):
        reply=input("Do you want to roll the dice again(s/no)?")
        if reply=='s':
            Dice()
        else:
            print("Thanks for rolling me,I will be ready to roll whenver you need me.")
            break
   
