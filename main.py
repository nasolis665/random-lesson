# random
from random import randint, choice
# # Python comes with a built in random library. There are a lot of functions included in this random library, so we will only 
# #show you two useful functions for now.
# print("random")
# first_random=randint(1,50)
# print(first_random)
dice1=randint(1,6)
dice2=randint(1,6)
dice3=randint(1,6)
dice4=randint(1,6)
dice5=randint(1,6)
rnd=randint(1,5)
my_gamble=dice1+dice2+dice3+dice4+dice5
print(my_gamble)
print(f"You're winning number is {rnd}")
if my_gamble == rnd:
  print("YOU WIN!")
elif my_gamble == 6:
  print("roll again")
elif (my_gamble % 2) == 1:
  print("You almost won")
elif (my_gamble > 12 and my_gamble < 18):
  print("you lost")
elif (my_gamble % 2) == 1:
  ("You're even")

dictionary1 = {}
# color = ['blue','red','green','turquoise','purple']
# my_random=choice(color)
# print(my_random)
my_characters=['rogue','elf','knight','ninja','samuri']
for character in my_characters:
  if rnd == my_characters[0]:
    print(character)
  else:
    print(rnd)
# from random import shuffle
# # This shuffles the list "in-place" meaning it won't return
# # anything, instead it will effect the list passed  
# shuffle(mylist)
# mylist

# [40, 10, 100, 30, 20]
# from random import randint
# # Return random integer in range [a, b], including both end points.
# randint(0,100)
# 25


# # Return random integer in range [a, b], including both end points.
# randint(0,100)
# 91



################################################random in python#################################################
# Random Practice #1
# Implement the randint() function from the random library that allows you to obtain an integer from 1 to 10, and store that value in a variable called random_number.


# Random Practice #2
# Implement the random() function from the random library to obtain a real number between 0 and 1, and store that value in a variable called random_number.


# Random Practice #3
# Use the random library's choice() method to get a random item from the list of names below, and store the chosen name in a variable called raffle.

# names = ["Samantha", "Carrie", "Chris", "Charlotte", "Richard"]
