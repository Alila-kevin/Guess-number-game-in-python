import random
compt=0
usert=0
same=0
saw={'R': "Rock", 'P': "paper", 'S': "Scissors"}
options=tuple(saw.keys())

while True:
    play =input("Do you want to play Rock/Paper/Scissor?(Y/N): ").upper()
    if play =='Y':
      useri=input("Choose: Rock/Paoer/Scissor(R/P/S): ").upper()
      rand=random.randint(0, 2)
      compi=options[rand]
      if useri not in options:
        print("Invalid choice")
      elif ((useri =='P' and compi =='R')
             or (useri =='S' and compi =='P')
             or (useri =='R' and compi =='S')):
        print(f"You win {saw[useri]}")
        print(f"computer chose {saw[compi]}")
        usert+=1
      elif useri==compi:
        print("You tie")
        print(f"You choose {saw[useri]}")
        print(f"computer choose {saw[compi]}")
        same +=1
      else:
       print("Computer won")
       print(f"You choose {saw[useri]}")
       print(f"computer choose {saw[compi]}")
       compt+=1
    elif play=='N':
      print("Goodby!")
      break
    else:
        print("invalid choice")
total=compt + same + usert

print(f"out of {total} you won {usert}, drow of {same} computer won {compt}")