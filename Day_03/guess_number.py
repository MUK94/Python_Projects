import random

num = random.randint(0, 20)
number_of_Guess = 6

for i in range(number_of_Guess):
    guess = int(input("Guess a number between 0 and 20: "))
    if guess == num:
        print("Congratulations 🎉, You nailed it the Number is " + str(guess))
        break
    elif guess < num:
        print("Your guess is too low")
    elif guess > num:
        print("Your guess is too high")
        
if guess != num: 
        print("Sorry! try again later the number I was thinking of was " + str(num))
        

# This is a Guess the Number game.

# guessesTaken = 0

# print('Hello! What is your name?')
# myName = input()

# number = random.randint(1, 20)
# print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

# for guessesTaken in range(6):
#     print('Take a guess.') # Four spaces in front of "print"
#     guess = input()
 
#     guess = int(guess)

#     if guess < number:
#         print('Your guess is too low.') # Eight spaces in front of "print"
#     if guess > number:
#         print('Your guess is too high.')
#     if guess == number:
#         break

# if guess == number:
#     guessesTaken = str(guessesTaken + 1)
#     print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
    
# if guess != number:
#     number = str(number)
#     print('Nope. The number I was thinking of was ' + number + '.')4