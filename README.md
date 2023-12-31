# Hangman
## Word Guessing Game

This is a simple word guessing game where the player guesses letters to find a secret word.

## Functions

### `check_guess(guess)`

This function takes a guessed letter as an argument and checks if the letter is in the word.

#### Parameters

- `guess` (str): The guessed letter.

#### Usage

'''python
check_guess('a')''' 

## Milestone 4: Guessing Letters and Handling Incorrect Guesses

In this milestone, we implemented the functionality to allow the player to guess letters and handle incorrect guesses appropriately.

### Implementation Details
1. Hangman Class:
- Defined a class called Hangman to represent the Hangman game.
2. __init__ Method:
- Implemented an __init__ method to initialize the game attributes:
- word_list: List of words for the game.
- num_lives: Number of lives the player has (default: 5).
- list_of_guesses: List to keep track of the guessed letters.
- word: Randomly selected word from the word_list.
- word_guessed: List representing the current state of guessed letters in the word.
- num_letters: Number of unique letters in the word.
3. check_guess Method:
- Implemented a method to check if the guessed letter is in the word:
- Converts the guessed letter to lowercase.
- Checks if the letter is in the word and updates word_guessed accordingly.
- Reduces num_letters by the count of guessed letter occurrences.
4. ask_for_input Method:
- Implemented a method to prompt the user for a letter guess and validate the input:
- Handles invalid input (non-alphabetic or more than one letter).
- Checks if the guess has already been tried.
- Calls the check_guess method for valid guesses.
Usage
To play the Hangman game, create an instance of the Hangman class with a word list and start guessing letters using the ask_for_input method.


## Task: Game Loop and Gameplay Management

In this task, we've implemented a game loop and gameplay management to handle user interaction and determine the game outcome.

### Implementation Details
1. play_game Function:
- Created a function called play_game to manage the Hangman game.
- Accepts a list of words (word_list) as a parameter.
2. Game Loop:
- Inside the play_game function, implemented a game loop using a while loop.
- Checked conditions to determine if the player won, lost, or needed to continue playing.
- Calls the ask_for_input method for the player to guess a letter if the game continues.
3. Game Outcome Messages:
- Printed appropriate messages based on the game outcome (win, loss, or ongoing game).
### Usage
To play the Hangman game, use the play_game function and pass a list of words as an argument.
