'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly chooses a 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.(1 for rock, 2 for paper, 3 for scissors and 4 for quit)
I don't want to be asked to quit each time. I will enter a 4 if I want to quit.
Add conditional statements to figure out who wins and keep the records
Each round tell me what the computer chose, what I chose and also if I won, lost or tied.
When the user quits print an end game message and their win/loss/tie record

'''
import random

done = False
win=0
lose=0
tie=0
a=0
while not done:
    a += 1
    answer= int(input("Enter 1 for rock, 2 for paper, 3 for scissors or 4 to quit: "))
    num = random.randint(1,3)
    if num==1 and answer== 1:
        print("computer chose: Rock")
        print("It's a tie")
        tie+=1

    elif num==1 and answer== 2:
        print("computer chose: Rock")
        print("You lose")
        lose+=1

    elif num==1 and answer== 3:
        print("computer chose: Rock")
        print("You win!")
        win+=1

    elif num==2 and answer==1:
        print("computer chose: Paper")
        print("You lose")
        win+=1

    elif num == 2 and answer == 2:
        print("computer chose: Paper")
        print("It's a tie")
        tie += 1

    elif num == 2 and answer==3:
        print("computer chose: Paper")
        print("You win!")
        win += 1

    elif num==3 and answer==1:
        print("computer chose: Scissors")
        print("You win!")
        win+=1

    elif num == 3 and answer == 2:
        print("computer chose: Scissors")
        print("You lose")
        lose += 1

    elif num==3 and answer==3:
        print("computer chose: Scissors")
        print("it's a tie")
        tie+=1

    elif answer == 4:
        print( )
        print("-------------------------------------------------------------")
        print()
        
        print("Thanks for playing")
        print("You tied", tie, "time(s)")
        print("You won", win, "time(s)")
        print("You lost", lose, "time(s)")
        done=True

print("You played Rock, Paper, Scissors",a,"times")













