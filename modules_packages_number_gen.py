# Learning about modules and packages and functions
import random
for i in range(3):
    print(random.randint(10,20))
    print(random.random())
members = ["you", "me", "him"]
leader = random.choice(members)
print(leader)

#program to roll a dice
class Dice:
    def roll(self):
        X = random.randint(1,6)
        Y = random.randint(1,6)
        return X,Y
dice = Dice()
print(dice.roll())