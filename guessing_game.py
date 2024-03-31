
# Import the random module.
import random

def guess(num1, num2):
    return int(input("Guess a number between {} and {}:   ".format(num1, num2)))
     
# Create the start_game function.
def start_game():
    high_score = 0
    number_of_tries = 0
    print("====================================\n  Welcome To The Guessing Game \n====================================")

    user_starting_number = int(input("Please choose a starting number:  "))
    user_ending_number = int(input("Please choose an ending number higher than, {}:  ".format(user_starting_number)))
    while user_starting_number > user_ending_number:
        print("Sorry that number is not higher than your starting number ({}). Try again".format(user_starting_number))
        user_ending_number = int(input("Choose a new number:   "))

    random_number = random.randint(user_starting_number, user_ending_number)
    print(random_number)
    user_guess = guess(user_starting_number, user_ending_number)
    while user_guess != random_number:
        number_of_tries += 1
        if user_guess > random_number:
            print("It's lower")
            guess(user_starting_number, user_ending_number)
        elif user_guess < random_number:
            print("It's higher")
    number_of_tries += 1
    if number_of_tries > 1:
        print("Your guess of {}, was the correct number. It took you {} tries".format(user_guess, number_of_tries))
    else: 
        print("Your guess of {}, was the correct number. It took you {} try".format(user_guess, number_of_tries))
    
    if high_score < number_of_tries:
        high_score = number_of_tries```
        print("Congrats you have the new high score, {}!".format(high_score))
    play_again = input("Would you like to try again?(y/n):   ")
    print(play_again)
    while play_again != "n" and play_again != "y":
        play_again = input("Congrats, would you like to try again?(y/n):   ")
    if play_again == "y":
        start_game()
    else:
        print("Thanks for playing, till next time")
    
    


#   2. Store a random number as the answer/solution.
#   3. Continuously prompt the player for a guess.
#     a. If the guess is greater than the solution, display to the player "It's lower".
#     b. If the guess is less than the solution, display to the player "It's higher".

#   4. Once the guess is correct, stop looping, inform the user they "Got it"
#      and show how many attempts it took them to get the correct number.
#   5. Let the player know the game is ending, or something that indicates the game is over.

# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.
start_game()