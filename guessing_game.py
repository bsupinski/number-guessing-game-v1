
# Import the random module.
import random

high_score = 0

def welcome_message(highscore):
    print("""
===========================
    Guess a Number Game
=========================== \n\n
""") 
    if highscore == None:
        print("There is no highscore currently")
    else:
        print("The highscore is currently {}".format(highscore))

def choose_number(msg):
    while True:
        try: 
            num = int(input(msg))
        except TypeError:
            print("Sorry that is not a whole number.")
        except ValueError:
            print("Sorry that is not a whole number.")
        else:
            return num
   
def check_higher_number(num1,num2):
    while num2 <= num1 + 3:
        print("Your first number was {}".format(num1))
        num2 = choose_number("Please choose your a number 4 numbers higher than first:   ")
    print(num1, num2)
    return random.randint(num1, num2)


def guess_number(num1, num2, randnum):
    total_guesses = 0
    guessed = choose_number("Please choose a number from {} to {}.   ".format(num1, num2))
    while guessed != randnum:                 
        total_guesses += 1
        if guessed < num1 or guessed > num2:
            print("{} is not in the number range.".format(guessed))
            guessed = choose_number("Please choose a number from {} to {}:   ".format(num1, num2))
        else:
            guessed = choose_number("{} is not the correct number. Try again:   ".format(guessed))
    total_guesses += 1
    return total_guesses

def new_highscore(guesses, highscore):
    if highscore == 0:
        high_score = guesses
        print("Congrats you guessed the number in {}. You have the new high score!".format(guesses))
    elif highscore < guesses:
        high_score = guesses
        print("Congrats you guessed the number in {}. You have the new high score!".format(guesses))
    else: 
        high_score = highscore
        print("Congrats you guessed the number in {}. But the high score ".format(guesses, high_score))
    return high_score
    


def start_game(highscore):
    welcome_message(highscore)
    first_number = choose_number("Please choose your lower number:   ")
    second_number = choose_number("Please choose your a number 4 numbers higher than first:   ")
    random_number = check_higher_number(first_number, second_number)
    total_guesses = guess_number(first_number, second_number, random_number)
    new_score = new_highscore(total_guesses, highscore)
    print(new_score)
    


start_game(high_score)