#shopping cart
foods =[]
prices = []
total = 0

while True:
    food= input("Enter a food to buy (q to quit): ").lower()
    if food =='q':
        break
    else:
        price = float(input(f"Enter the price of {food} : $ "))
        foods.append(food)
        prices.append(price)
print("----------Cart---------")
for food in foods:
    print(food, end=" ")
    
for price in prices:
    total +=price
    
print()    
print(f"Your ttotal is ${total}")