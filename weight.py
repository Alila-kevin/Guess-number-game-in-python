print("**************************************************************************")
print("Weight Conversion System: Kilograms to Grams or Grams to Kilograms")
print("**************************************************************************")

weight = float(input("Enter weight: "))  # Convert input to float for calculations
print("_______________________________________________________")
unit = input("Enter unit of the weight (K for Kilograms, g for Grams): ")

if unit == 'K' or unit == 'k':
    grams = weight * 1000  # Convert kilograms to grams
    print(f"{weight} Kilograms is {grams} Grams")
    print("_______________________________________________________")
elif unit == 'g' or unit == 'G':
    kilograms = weight / 1000  # Convert grams to kilograms
    print(f"{weight} Grams is {kilograms} Kilograms")
    print("_______________________________________________________")
else:
    print("_______________________________________________________")
    print("Please enter the correct unit")
