
# Import the random module.
import random

def guess(num1, num2):
    try:
        return int(input("Guess a number from {} and {}:   ".format(num1, num2)))
    except ValueError:
        print("Please choose a whole number")
    except TypeError:
        print("Please choose a whole number")
     
# Create the start_game function.
def start_game():
    high_score = 0
    number_of_tries = 0
    print("====================================\n  Welcome To The Guessing Game \n====================================")
    #User chooses two numbers
    try:
        user_starting_number = int(input("Please choose a starting number:  "))
    except ValueError:
        print("Please choose a whole number")
    else:
        try:
            user_ending_number = int(input("Please choose an ending number higher than, {}:  ".format(user_starting_number)))
        except ValueError:
            print("Please choose a whole number")
        else:
            #Check to make sure first number is smaller than second number
            while user_starting_number + 2 > user_ending_number:
                print("Sorry that number is not high enough than your starting number to have numbers inbetween ({}). Try again".format(user_starting_number))
                try:
                    user_ending_number = int(input("Choose a new number:   "))
                except ValueError:
                    print("Please choose a whole number")
            else:
                #Choose a random number from both numbers
                try:
                    random_number = random.randint(user_starting_number, user_ending_number)
                except ValueError:
                    print("Please choose a whole number")
                else:
                    #User guesses a number, till correct
                    try:
                        user_guess = guess(user_starting_number, user_ending_number)
                    except ValueError:
                        print("Please guess a whole number")
                    else:
                        try:
                            while user_guess != random_number:
                                number_of_tries += 1
                                if user_guess > random_number:
                                    print("It's lower")
                                elif user_guess < random_number:
                                    print("It's higher")
                                else:
                                    print("Not a number")
                                
                                user_guess = guess(user_starting_number, user_ending_number)
                            number_of_tries += 1
                        except TypeError:
                            print("That's not a number please start the game again.")
                        else:
                            #Print winning message
                            if number_of_tries > 1:
                                print("Your guess of {}, was the correct number. It took you {} tries".format(user_guess, number_of_tries))
                            else: 
                                print("Your guess of {}, was the correct number. It took you {} try".format(user_guess, number_of_tries))
                            #Print high score message if new high score.
                            if high_score < number_of_tries:
                                high_score = number_of_tries
                                print("Congrats you have the new high score, {}!".format(high_score))
                            play_again = input("Would you like to try again?(y/n):   ")
                            print(play_again)
                            while play_again != "n" and play_again != "y":
                                print(play_again)
                            if play_again == "y":
                                start_game()
                            else:
                                print("Thanks for playing, till next time")

start_game()