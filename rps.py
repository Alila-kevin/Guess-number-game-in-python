import random

userw = 0
compw = 0
options = ["rock", "paper", "scissors"]

while True:
    userin = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if userin == 'q':
        break  # Use break instead of quit() for a cleaner exit

    if userin not in options:
        print("Please choose Rock, Paper, or Scissors.")
        continue  # Continue to the next iteration if the input is invalid

    randno = random.randint(0, 2)
    compin = options[randno]
    print(f"The computer chose: {compin}")  # Show the computer's choice

    # Determine the winner
    if (userin == 'paper' and compin == 'rock') or \
       (userin == 'scissors' and compin == 'paper') or \
       (userin == 'rock' and compin == 'scissors'):
        print("You are a winner!")
        userw += 1
    elif userin == compin:
        print("It's a tie!")
    else:
        print("You lose.")
        compw += 1

# Final results
print("You won", userw, "times.")
print("The computer won", compw, "times.")
print("Goodbye!")
