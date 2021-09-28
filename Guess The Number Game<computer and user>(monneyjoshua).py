import random

'''
This is a 2 in 1 guessing game in which the computer randomly stores a single number 
from a limited range of numbers and the user is allowed to figure it out and for the 
2nd one the user is allowed to store a secret number where the computer is allowed
to guess that out
'''


# This program was programmed by Monney Joshua in python3

def user_guess(x):  # This is the first guessing game by which the computer stores a value for the user to guess
    random_number = random.randint(1, x)
    guess = 0
    print("\nGUESS THE NUMBER GAME<USER>\n")
    print("the computer stores a secret number within the range of numbers you just entered\nGuess it out\n")
    while guess != random_number:
        try:  # This is an exception handler that makes sure the user inputs an integer
            guess = int(input(f"Enter a guess between 1 to {x}: "))
        except ValueError:  # an error is caught by the ValueError exception
            print("<Please enter an integer value>\n")
            continue
        if guess < random_number:
            print("Wrong guess,too low:\n ")
        elif guess > random_number:
            print("Wrong guess,too high:\n ")

    print(
        f"\nYay! you guessed the computer's secret number ,{guess}, correctly!!")  # This gets printed out when you
    # guessed the number right
    while True:
        play_again = input("\nPlay again Y/N: ")  # This is a play again command,you can play again or terminate the
        # program
        if play_again.lower() == "y":
            start_game()
        elif play_again.lower() == "n":
            quit()
        else:
            print("Please enter a 'y' for yes or an 'n' for no")
            continue


def computer_guess(x):  # This is the 2nd guessing game which the user stores a value for the computer to guess
    high = x
    low = 1
    feedback = ""
    secret_number = int(input("\nInput your secret number(this should be within the range of number you entered): "))
    # You are allowed to enter your secret number to verify if the computer has guessed your secret number
    while True:
        if secret_number > x:  # The if else statement makes sure the user stores a value within the range of numbers
            secret_number = int(input(" Beyond range.Input your secret number again:\n "))
        else:
            break
    while feedback != "c":
        guess = random.randint(low, high)

        feedback = input(
            f"is the number {guess} guessed by the computer too high(H),too low(L) or correct(C): ").lower()
        # h represent high,l represent low and c represent correct,user should input these h,l and c
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback != "c" and feedback != "l" and feedback != "h":
            print("<Please input the character 'L' for low,'H' for high or 'C' for correct ")
    if secret_number == guess:  # This if else statement makes sure that the computer truly guessed your secret number
        print(f"Yay! the computer guessed your secret number ,{guess}, correctly")
    else:
        print("\nuser has made a mistake choosing the correct('c') option,the computer hasn't guessed your secret "
              "number\n")  # This if else makes sure that if the user picks the 'c' option,the number guessed by the
        # computer is actually the same as the secret number of the user else it outputs a mistake
        computer_guess(x)

    while True:
        play_again = input("\nPlay again Y/N: ")  # This is a play again command,you can play again or terminate the
        # program
        if play_again.lower() == "y":
            start_game()
        elif play_again.lower() == "n":
            quit()
        else:
            print("Please enter a 'y' for yes or an 'n' for no")
            continue


def start_game():  # This is the function where the program initializes
    print("\nGUESS THE NUMBER GAME\n")
    print("(a) Guess the number(user)")
    print("(b) Guess the number(computer)")
    choice = input("\nPlease select a guessing game(a or b): ").lower()
    if choice == "a":
        while True:
            try:
                enter = int(input("\ninput an integer(the number you input will be used by the computer for the range "
                                  "of numbers): "))
                user_guess(enter)
            except ValueError:
                print("<Please input an integer value>")
            continue

    elif choice == "b":
        while True:
            try:
                enter = int(input("\ninput an integer(the number you input will be used by the computer as a range to "
                                  "figure out your secret number): "))
            except ValueError:
                print("<Please input an integer value>")
                continue
            while True:

                try:

                    computer_guess(enter)
                    break
                except ValueError:
                    print("<Out of range>")
            break
    else:
        print("<Please input a or b>")
        start_game()


start_game()  # This is the start_game() function which needs to be called always for the game to execute
