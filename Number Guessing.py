import random
import math

lower = int(input("Enter lower integer: "))
upper = int(input("Enter upper integer: "))
random_number = random.randint(lower, upper)
chances = round(math.log(upper - lower + 1, 2))
print(f"You've only {chances} chances to guess the integer!\n")
count = 0
while count < chances:
    count += 1
    guess = int(input("Enter a number: "))

    if random_number == guess:
        print(f"Congratulations!, You won in {count} try.")
        break
    elif random_number > guess:
        print("You guessed too low!")
    elif random_number < guess:
        print("You guess too high!")
    else:
        print("Please guess only an integer: ")

if random_number != guess:
    print(f"\nThe number is {random_number}")
    print("\tBetter Luck Next time!")
