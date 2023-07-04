# Bagel Game
import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print(f''' 
          A deductive logic game by AI Sweigart
          
          I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
            Try to guess what it is. Here are some clues:
            When I say: That means:
            Pico One digit is correct but in the wrong position.
            Fermi One digit is correct and in the right position.
            Bagels No digit is correct.
            For example, if the secret number was 248 and your guess was 843, the
            clues would be Fermi Pico.
        ''')
    
    while True:
        secretNum = getSecretNum() # Function to generate the number
        print('I have Thought up a number.')
        print(f' You have {MAX_GUESSES} guesses to get it.')
        
        # Store and Initialize number of guesses
        numGuesses = 1
        
        while numGuesses <= MAX_GUESSES:
            guess = '' # user guess
            
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{numGuesses}: ')
                guess = input('> ')
            
            # Give player clues
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1
            
            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print(f'The answer was {secretNum}.')
        
        # Keep playing if they want
        print('Do you wanna play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')
    
# Function for generating the 3 digit number 
def getSecretNum():
    
    """Returns a string made up of NUM_DIGITS unique random digits"""
    numbers = list('0123456789')
    random.shuffle(numbers)
    
    # Get the first 3 digit in the list
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

# Function for getting clues
def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess and secret number pair."""
    if guess == secretNum:
        return 'You got it!'
    
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # A correct digit is in the incorrect place.
            clues.append('Pico')
    
    if len(clues) == 0:
        # No correct digits at all 
        return 'Bagels' 
    
    else:
        '''Sort the clues into alphabetical order so their original order doesn't give information away'''
        clues.sort()
        # Make a single string from the list of string clues
        return ' '.join(clues)
    
# If the program is run (instead of imported), run the game
if __name__ == '__main__':
    main()