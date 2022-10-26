'''
COIN TOSS PROGRAM
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''
import random

heads=0
tails=0
for f in range(50):
    flip= random.randint(0,1)
    if flip==0:
        print("Heads")
        heads+=1
    elif flip==1:
        print("Tails")
        tails+=1
print("The total number of Heads outcomes:",heads)
print("The total number of Tails outcomes:",tails)










