try:
    user_starting_number = int(input("Please choose a starting number:  "))
except ValueError:
    print("Please pick a whole number")
else:
    user_ending_number = int(input("Please choose an ending number higher than, {}:  ".format(user_starting_number)))