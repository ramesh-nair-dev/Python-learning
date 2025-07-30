secretWord = "jon"
countOfGuesses = 0
numberGuess = 3

def getGuess():
    guess = input("Enter your guess: ")
    return guess

while countOfGuesses <= numberGuess:
    guess = getGuess()
    countOfGuesses += 1

    if(countOfGuesses <= numberGuess):
        if(countOfGuesses == numberGuess-1):
            print(f"You have {numberGuess - countOfGuesses} guesses left.")

        if guess.lower() == secretWord:
            print("Congratulations! You guessed the word correctly.")
            break

        else:
            print("Incorrect guess, try again !")
        
    else:
        print("Sorry, you have used all your guesses. The correct word was:", secretWord)
        print("Game over!")
        break

# This code implements a simple word guessing game.
# The player has a limited number of guesses to find the secret word.
# The player is prompted to enter their guess, and the program checks if it matches the secret word.
# If the guess is correct, a congratulatory message is displayed.
# If the guess is incorrect, the player is informed and given another chance until they run out of guesses.
# If the player runs out of guesses, the correct word is revealed and the game ends.
# The game uses a while loop to manage the guessing attempts and provides feedback on the number of guesses left.