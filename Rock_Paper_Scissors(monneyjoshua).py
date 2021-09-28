import random


# This is a rock paper scissors game programmed by Monney Joshua in python3
# This game was introduced to me as a kid by my lovely girl "Valerie McBean"
def rock_paper_scissors():
    user_score = 0
    computer_score = 0
    while True:

        print("\nROCK PAPER SCISSORS\n")
        print(f"SCORES:\t\t\t\t\t\t\t\t\tuser = {user_score}, computer = {computer_score}\n")
        user = input("Your choice('r' for rock,'p' for paper and 's' for scissors): ").lower()
        computer = random.choice(['r', 'p', 's'])

        if user == computer:  # These are nested if statements for the condition of same occurrences
            if user == 'r' and computer == 'r':
                print("You picked rock\t\t\t\t\t\t\tcomputer picked rock\n\t\t\t\t\tIT'S A TIE\n")
            if user == 'p' and computer == 'p':
                print("You picked paper\t\t\t\t\t\t\tcomputer picked paper\n\t\t\t\t\tIT'S A TIE\n")
            elif user == 's' and computer == 's':
                print("You picked scissors\t\t\t\t\t\t\tcomputer picked scissors\n\t\t\t\t\tIT'S A TIE\n")

        elif user == 'r' and computer == 'p':
            print("You picked rock\t\t\t\t\t\t\tcomputer picked paper\n\nYou are wrapped!\tYOU LOSE\n")
            computer_score += 1
        elif user == 'r' and computer == 's':
            print("You picked rock\t\t\t\t\t\t\tcomputer picked scissors\n\nComputer is crushed!\tYOU WIN!!\n")
            user_score += 1
        elif user == 'p' and computer == 'r':
            print("You picked paper\t\t\t\t\t\t\tcomputer picked rock\n\nComputer is wrapped!\tYOU WIN!!\n")
            user_score += 1
        elif user == 'p' and computer == 's':
            print(
                'You picked paper\t\t\t\t\t\t\tcomputer picked scissors\n\nYou are cut into pieces!\tYOU LOSE\n')
            computer_score += 1
        elif user == 's' and computer == 'p':
            print("You picked scissors\t\t\t\t\t\t\tcomputer picked paper\n\nComputer is cut into pieces!\tYOU "
                  "WIN!!\n")
            user_score += 1
        elif user == 's' and computer == 'r':
            print("You picked scissors\t\t\t\t\t\t\tcomputer picked rock\n\nYou are crushed!\tYOU LOSE\n")
            computer_score += 1
        else:  # This else statement makes sure the user inputs a 'r','p' or 's' else it restarts the game
            print("\nPlease enter 'r','p' or 's' for rock paper scissors\n\n")
            continue
        # The score list for the end of every game play
        print(f"SCORES:\t\t\t\t\t\t\t\t\tuser = {user_score}, computer = {computer_score}\n")

        # This play again function allows the while loop to keep looping if only
        while True:
            play = input("play again y/n: ")
            if play.lower() == 'y':  # the user selects yes else selecting no would break the loop
                break
            elif play.lower() == 'n':
                break
            else:
                print("Please enter a 'y' for yes or an 'n' for no")
                continue
        if play == 'y':
            print()
        else:
            break


rock_paper_scissors()  # This is the game function to start the game
