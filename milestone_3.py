import random


favorite_fruits = ['Apple', 'Banana', 'Orange', 'Strawberry', 'Mango']


word_list = favorite_fruits


guess = ""


word = random.choice(word_list)


def check_guess(guess):
    # Step 2: Convert the guess into lower case
    guess = guess.lower()
    
    # Step 3: Move the code to check if the guess is in the word
    # (Assuming you have a variable 'word' containing the word to guess)
    if guess in word:
        print("Guess is in the word!")
    else:
        print("Guess is not in the word.")


def ask_for_input():
    # Step 2: Move the code to check if the input is a valid guess
    while True:
        guess = input("Enter your guess: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        else:
            break  # Exit the loop if the input is valid

    # Step 3: Call check_guess function to check if the guess is in the word
    check_guess(guess)


# Step 4: Call the ask_for_input function to test the code
ask_for_input()