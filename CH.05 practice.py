#LOOPING!!!!!!
import random
# for i in range(100,-1,-2):
#     print(i)
#
# for n in [2,6,1,7,0,9]:
#     print(n)
# for p in ("Hi Marc Hermon"):
#     print(p)
#
# for i in range(3):
#     print("A")
#
# for i in range(3):
#     print("A")
#     for j in range(3):
#         print(j)
# print("done")

# total = 0
# for i in range(1,1001):
#     total+=i
# print("the total is:",total)
#
# a=0
# for i in range(10):
#     a+=1
#     for j in range(10):
#         a+=1
# print(a)
#
# for i in range(10)
#     print(i)

#while loop
# i = 1
# while i<=2**32:
#     print(i)
#     i*=2

#while not loop
# done = False
# pereserverance = 0
# while not done:
#     quit = input("Do you want to quit?")
#     if quit.lower()=="y":
#         done = True
#     else:
#         pereserverance+=1
# print("goodbye! Your perserverance level is",pereserverance)
#
# for i in range(10):
#     num = random.random()*5+10
#     print(num)

# for i in range(10):
#     nums = random.randrange(1,101)
#     print(nums)

#guess the number
#
# over = False
# secret_num = random.randint(1,100)
# while not over:
#     guesses = 0
#     guess = int(input("guess the random number:"))
#     guesses+=1
#     if guess== secret_num:
#         print("you found the random number")
#     elif guess<secret_num:
#         print("Too LOW")
#     elif guess>secret_num:
#         print("Too HIGH")
#
# print("Goodbye! It took you",guesses,"guesses to find the random number")
#
# for leter in "Death Star":
#     if letter== " ":
#         continue
#     print('Current letter: ',letter)
#
# var= 10
# while var>0:
#     var+=1
#     if var%2 !=0:
#         continue
#     print("Current Variable value: ",var)
# print("Goodbye!")


print("\033[1;36;1m \n")

print("How are you")

samplelist=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
x=random.choice(samplelist)
print(x)
if x==5:
    print("You have found the oasis")

print("\033[1;35;1m \n")
print("hey")