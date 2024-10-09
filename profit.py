def calculate_interest(deposit, rate, n, time):
    # Calculate compound interest
    amount = deposit * (1 + (rate / 100) / n) ** (n * time)
    return amount

print("*******************************************************************")
print("                COMPOUND INTEREST CALCULATOR                          ")
print("*******************************************************************")
print("                                                                     ")
print("###################################################################")

# Get user inputs
deposit = float(input("The principal investment amount (the initial deposit or loan amount): "))
print("______________________________________________________________________________________")
rate = float(input("Percentage of the annual interest rate: "))
print("______________________________________________________________________________________")
n = int(input("The number of times that interest is compounded per year: "))
print("______________________________________________________________________________________")
time = float(input("The number of years the money is invested or borrowed: "))
print("______________________________________________________________________________________")
print("                                                                     ")
print("*******************************************************************")

# Calculate and display the result
final_amount = calculate_interest(deposit, rate, n, time)
percentage_increase = ((final_amount - deposit) / deposit) * 100  # Calculate percentage increase

print(f"The amount after {time} years will be: {final_amount:.2f}")
print(f"The percentage increase over the initial deposit is: {percentage_increase:.2f}%")
print("*******************************************************************")
