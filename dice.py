import random

n =True
while n:
    option = input("Do you want to roll the dice? (Y/N): ").upper()
    c1 = random.randint(1, 6)
    c2 = random.randint(1, 6)
    if option=='Y':
      print(f"({c1}, {c2})")
      
    elif option=='N':
     print("Thank for playing")
     break
    else:
      print("invailid choice")