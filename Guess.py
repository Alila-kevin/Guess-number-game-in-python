import random

# Get the highest number range from the user
a = input("Give the highest number range: ")
if a.isdigit():
    a = int(a)
    if a <= 0:
        print("Please give a number greater than zero.")
        quit()
else:
    print("Please give a valid number.")
    quit()

# Generate a random number between 0 and the specified range
ranno = random.randint(0, a)
guesses = 0

# Start the guessing loop
while True:
    b = input("Please give your guess: ")
    if b.isdigit():
        b = int(b)
        guesses += 1  # Count the number of guesses

        if b == ranno:
            print(f"You got it! The number was {ranno}. It took you {guesses} guesses.")
            break
        elif b > ranno:
            print("Your guess is higher.")
        else:
            print("Your guess is lower.")
    else:
        print("Please type a number next time.")
print("winner")

