def ctok(temp):
    return round(temp + 273.15, 2)

def ktoc(temp):
    return round(temp - 273.15, 2)

def ctof(temp):
    return round(9/5 * temp + 32, 2)

def ftoc(temp):
    return round(5/9 * (temp - 32), 2)

def ftok(temp):
    return round(5/9 * (temp - 32) + 273.15, 2)

def ktof(temp):
    return round((temp - 273.15) * 9/5 + 32, 2)

# Lists to hold options and corresponding functions
options = [
    "Celsius to Kelvin",
    "Kelvin to Celsius",
    "Celsius to Fahrenheit",
    "Fahrenheit to Celsius",
    "Fahrenheit to Kelvin",
    "Kelvin to Fahrenheit"
]

functions = [
    ctok,
    ktoc,
    ctof,
    ftoc,
    ftok,
    ktof
]

while True:
    print()
    print("**** TEMPERATURE CONVERSION (CELSIUS, KELVIN, FAHRENHEIT) *****")
    print()

    print("Please select the option for temperature conversion")
    print(".............................................................")
    for i, option in enumerate(options, start=1):
        print(f"Option {i}: {option}")
    
    unit = input("Enter your option: ")
    temp = float(input("Enter the temperature: "))

    # Check if the input is valid
    if unit.isdigit() and 1 <= int(unit) <= len(options):
        index = int(unit) - 1
        result = functions[index](temp)
        print(f"The result is: {result} {'K' if index % 2 == 0 else '°C' if index == 1 or index == 3 else '°F'}")
    else:
        print(f"{unit} is an invalid option. Please try again.")
    
    another = input("Do you want to perform another conversion? (yes/no): ").strip().lower()
    if another != 'yes':
        break

print()
print("################# THANK YOU FOR USING OUR SYSTEM #################")
