import random

print("Number guessing Game")

range = input("please enter the range: ")

if range.isdigit() and int(range) > 0:
   
   comp = random.randint(1, int(range) + 1)
else:
   print("Please give a number")
guesses=0

while True:
    guess =input(f"Enter your guess betwen 1 and {range}: ")
    guesses +=1
    if guess.isdigit() and int(guess) >0:
        
        guess = int(guess)
        if guess > comp:
            print(f"{guess} is too high")
        elif guess < comp:
            print(f"{guess} is too low")
        else:
            print(f"Congratulations answer is {guess}")
            break
    else:
        print("Please enter valid number")
print(f"It has taken you {guesses} guesses to win")