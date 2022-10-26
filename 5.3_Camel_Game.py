'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
print("\033[1;33;1m \n")
print("You (Frodo) and Sam have just escaped the Orc attack in the woods of Amon Hen\nand have found yourself making the journey together to the land of Mordor\nto cast the one ring into Mount Doom\nBut, the orcs are not far behind you and Sam can only carry you so far\n so you must make decisions wisely so as not to be caught")
print("----------------------------------------------------------------------------")
done= False
miles_traveled=0
thirst=0
tiredness=0
frodo_tiredness=0
orc_distance=-20
drinks=5
add = random.randint(7, 14)


while not done:
    print("\033[1;33;1m \n")
    print("A. Drink Water\nB. Ahead Moderate speed\nC. Ahead full speed\nD. Stop for the night\nE. Status check.\nQ. Quit.")
    answer = str(input("What would you like to do? "))
    print()
    print("--------------------------------------------------------------------------------")

    samplelist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
    x = random.choice(samplelist)
    close = miles_traveled - orc_distance


    if answer.lower()=="d" and tiredness > 8 and miles_traveled >= 180 and thirst <= 3:
        frodo_tiredness=0
        print("\033[1;35;1m \n")
        print("You must rest by yourself tonight, hopelessly clutching your blanket as you sleep\n scared and afraid, missing the comfort of your dead friend")
        orc_distance+=add

    elif answer.lower()== "d":
        tiredness=0
        print("\033[1;36;1m \n")
        print("You and Sam are both happy and well rested to continue your journey")
        orc_distance+=add

    elif  answer.lower()== "c" and tiredness > 8 and miles_traveled >= 180 and thirst <= 3:
        frodo_go = random.randint(5,10)
        print("\033[1;35;1m \n")
        print("You traveled",frodo_go,"miles")
        thirst+=1
        frodo_tired=random.randint(1,3)
        frodo_tiredness+=frodo_tired
        orc_distance+=add
        miles_traveled+=frodo_go

    elif answer.lower()== "c":
        forward=random.randint(10,15)
        print("\033[1;36;1m \n")
        print("You traveled",forward,"miles")
        thirst+=1
        tired=random.randint(1,3)
        tiredness+=tired
        orc_distance+=add
        miles_traveled+=forward

    elif answer.lower()=="b" and tiredness > 8 and miles_traveled >= 180 and thirst <= 3:
        frodo_moderate = random.randint(3,5)
        print("\033[1;35;1m \n")
        print("You traveled",frodo_moderate,"miles")
        thirst+=1
        frodo_tiredness+=1
        orc_distance+=add
        miles_traveled+=frodo_moderate

    elif answer.lower()== "b":
        go = random.randint(5,12)
        print("\033[1;36;1m \n")
        print("You traveled",go,"miles")
        thirst+=1
        tiredness+=1
        orc_distance+=add
        miles_traveled+=go

    elif answer.lower()== "a":
        drinks-=1
        thirst=0
        print("\033[1;36;1m \n")
        print("You now have",drinks," drinks left")

    elif answer.lower()=="e" and tiredness > 8 and miles_traveled >= 180 and thirst <= 3:
        print("\033[1;35;1m \n")
        print("drinks:",drinks, "")
        print("\033[1;36;1m \n")
        print("Sams tiredness: BROS DEAD")
        print("\033[1;35;1m \n")
        print("Frodos tiredness:",frodo_tiredness, "")
        print("miles traveled:",miles_traveled, "")
        print("The orcs are",close,"miles behind you")
        print("thirst:",thirst, "")

    elif answer.lower()=="e":
        print("\033[1;36;1m \n")
        print("drinks:",drinks,"")
        print("Sams tiredness:",tiredness,"(If over 5, pass out. if over 8, DEAD")
        print("Frodos tiredness:",frodo_tiredness,"")
        print("miles traveled:",miles_traveled,"")
        print("The orcs are", close, "miles behind you")
        print("thirst:",thirst,"")

    elif answer.lower()=="q":
        done=True
        break

    if tiredness >= 8 and miles_traveled >= 180:

        print("\033[1;35;1m \n")
        left = 200 - miles_traveled
        print("Sam, your trusted companion and transporter, has died of tiredness\nbut there is only", left,"miles between you and morder\nso now you must make the last push of the journey alone and at a slower pace\nto fulfill you promise and destroy the one ring\noh and don't get caught by the orcs")


    if thirst>=4 and thirst<=6:
        print("\033[1;31;1m \n")
        print("You are thirsty")

    if thirst>6:
        print("\033[1;31;1m \n")
        print("You died of thirst!")
        done= True
        break

    if tiredness>3 and tiredness<8:
        print("\033[1;31;1m \n")
        print("You and Sam are getting tired")

    elif tiredness>5 and tiredness<8:
        print("\033[1;31;1m \n")
        print("Due to lack of rest, you have passed out ")

    elif tiredness>8 and miles_traveled<=180:
        print("\033[1;31;1m \n")
        print("Sam, your trusted companion and transporter, has died of tiredness\nsince you have lost your mode of transportation you can no longer continue your journey\nand must head home, if you can even make that trip.")
        done = True
        break

    if orc_distance>=miles_traveled:
        print("\033[1;31;1m \n")
        print("The orcs have caught up to you! GAME OVER.")
        done= True
        break

    if close<=14:
        print("\033[1;31;1m \n")
        print("The orcs are getting close!")

    if miles_traveled>=200 and tiredness<8:
        print("\033[1;36;1m \n")
        print("Congratulations you have made it to Mordor and have cast the ring into the fires of mount doom\n You have beat the game.")
        done=True
        break

    elif miles_traveled>=200 and tiredness>8:
        print("\033[1;36;1m \n")
        print("Congradulations, by your self, you have managed to complete the rest of your journey without Sam\n although he died making the trip, he helped make Middle Earth a better and more peaceful place\nAnd you fulfilled your promis and destroyed the one ring and defeated evil\nYou have beat the game. ")

    if x==5:
        print("\033[1;36;1m \n")
        print("You have found an Oasis!")
        print("You fill up your canteen, rest, and are no longer thirsty ")
        drinks=5
        thirst=0
        tiredness=0

    if x==19:
        print("\033[1;32;1m \n")
        miles_traveled+=20
        print("Congrats, you have found magical berries along a path\n the berries have given you super speed of +20 miles")

    if x==30:
        print("\033[1;31;1m \n")
        print("Oh no, Sam has twisted his ankle on a rocky path\n Forcing you to stop for the night for him to recover ")
        orc_distance+=15
        print("While recovering, the orcs gained 15 miles on you")


print("Thanks for playing!")














