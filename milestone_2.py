import random
my_fav_fruits = ['Apple', 'Banana', 'Orange', 'Strawberry', 'Mango']
word_list = my_fav_fruits
word = random.choice(word_list)
print(word)

guess = input("Please enter a single letter: ")
if len(guess) == 1:
    print("Good guess!")

else:
    print ("Oops! That is not a valid input.")



