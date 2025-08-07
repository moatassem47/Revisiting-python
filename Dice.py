import random 

def RollDice():
    numberofrolls = int(input("how many times do u want to roll?"))
    for i in range(1,numberofrolls+1):
     Dice = random.randint(1,100)
     print(Dice)

RollDice()
