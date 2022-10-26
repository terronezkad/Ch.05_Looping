  #Sign your name: Kadin Terronez

import random
'''
 1. Make the following program work.
   '''  
print("This program takes three numbers and returns the sum.")
total = 0
for i in range(3):
        x = int(input("Enter a number: "))
        total+=x
print("The total is:", total)
  


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
for n in range(2,101,2):
        print(n)




'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
h=10
while h>-1:
    print(h)
    h-=1
print("Blast Off")





'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''

print(random.randint(1,10))

'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
total=0
equal=0
positive=0
negative=0
for r in range(7):
    random = int(input("Enter a number: "))
    total+=random
    if random<0:
        negative+=1
    elif random>0:
        positive+=1
    else:
        equal+=1
print("---------------------------------------------------------------------")
print("-------------------------------REPORT--------------------------------")
print("---------------------------------------------------------------------")

print("the sum of the numbers is:",total)
print("The amount of numbers equal to zero is:",equal)
print("The amount of positive numbers is:",positive)
print("The amount of negative numbers is:",negative)

