import random

class Hangman:
    
   def check_guess(self, guess):
        """
        Check if the guessed letter is in the word and update word_guessed.

        Parameters:
        guess (str): The guessed letter.
        """
        # Step 1: Convert the guessed letter to lower case
        guess = guess.lower()

        # Step 2: Create an if statement that checks if the guess is in the word
        if guess in self.word:
            # In the body of the if statement, print a message
            print(f"Good guess! {guess} is in the word.")

            # Update word_guessed by replacing underscores with the guessed letter
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess

            # Reduce the variable num_letters by the count of guessed letter occurrences
            self.num_letters -= self.word.count(guess)
        else:
            # If the guess is not in the word, reduce num_lives and provide messages
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        
        def play_game(word_list):
            num_lives = 5

            game = Hangman(word_list)

            game = Hangman(word_list, num_lives)
            
            while True:
                if game.num_lives == 0:
                    print("You lost!")
                    break
                
                elif game.num_letters > 0:
                    game.ask_for_input()
                else:
                    
                    print("Congratulations! You won the game!")
                    break

            