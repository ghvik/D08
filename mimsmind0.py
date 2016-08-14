#!/usr/bin/env python
#
# Mims Place-in Exam 1
# Mastermind
#
# usage: python mimsmind0.py [length]
##############################################################################

from random import randint
import sys

def start_prompt():
    """Asks the user to guess a random number"""
    
    # Checks to see if the program is run with extra arguments
    # else provides a default argument
    if len(sys.argv) > 1:
        num_digits = int(sys.argv[1])
    else:
        num_digits = 1
    secret_number = randint(10**(num_digits - 1), 10**num_digits - 1)
    guesses = 0
    congrats = ("Congratulations! You guess the correct number in {} {}."
        .format(guesses, "try" if guesses==1 else "tries"))
    while True:
        user_input = input("Please guess a {}-digit number or type 'done' to quit: ".format(num_digits))
        if user_input == "done":
            break
            
        # Validate user input
        try:
            user_input = int(user_input)
        except ValueError as e:
            print(e, "Please type non-word numerals.")
        else:
            guesses += 1
            # print("The user has guessed {} times".format(guesses))
            if user_input > secret_number:
                print("Sorry, you have to guess a lower number.")
            elif user_input < secret_number:
                print("Sorry, you have to guess a higher number.")
            else:
                print(("Congratulations! You guessed the correct number in {} {}!"
                    .format(guesses, "try" if guesses==1 else "tries")))
                break
    
def main():
    start_prompt()

if __name__ == "__main__":
    main()