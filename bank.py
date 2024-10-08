def show_balance():
     print(f"your balance is {balance}")
def deposite():
     amount = float(input("input the amount to deposite"))
     if amount < 0:
          print("please the amount should be higher than 0")
          return 0

     else:
          return amount
     
def withdrow():
      amount = float(input("input the amount to withdrow"))
      if amount > balance:
          print("The amount you enter is more than your balance")
          return 0

      else:
          return amount
     

balance = 0
isrunning = True

while isrunning:
    print("***************************")
    print("welcome to bank my cash") 
    print("***************************") 
    print("Press 1: To check your balance")
    print("Press 2: To deposit")
    print("Press 3: To withdrow")
    print("Press 4: To Exit")

    choice = input("input 1-4  ")
    if choice == '1':
          print("***************************")
          show_balance()
          print("***************************")
    elif choice == '2':
         print("***************************")
         balance +=deposite()
         print("***************************")
    elif choice == '3':
         print("***************************")
         balance -=withdrow()
         print("***************************")
    elif choice == '4':
         isrunning = False
    else:
         print("***************************")
         print("give a valid number between 1 to 4")
         print("***************************")