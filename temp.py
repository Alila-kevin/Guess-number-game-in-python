#Celsius to Kelvin + 273.15
#kelvin to celsius -  273.15
#Celsius to Fahrenheit	° F = 9/5 * (temp) + 32
#Fahrenheit to Celsius	° C = 5/9 * (temp - 32)
#Fahrenheit to Kelvin	K = 5/9 * (temp - 32) + 273
#kelvin to fahrenheit °F = (temp − 273.15) × 1.8 + 32

def ctok(temp):
    temp = round(temp + 273.15, 2)
    ans = print(f"The temperature in Kelvin is: {temp} K")
    return ans

def ktoc(temp):
    temp = round(temp - 273.15, 2)
    ans = print(f"The temperature in Celsius is: {temp} C")
    return ans
def ctof(temp):
    temp = round(9/5 * ( temp) + 32, 2)
    ans = print(f"The temperature in Fahrenheit is: {temp} F")
    return ans
def ftoc(temp):
    temp = round(5/9 * (temp - 32), 2)
    ans = print(f"The temperature in celsius is: {temp} C")
    return ans
def ftok(temp):
    temp = round(5/9 * (temp - 32) + 273, 2)
    ans = print(f"The temperature in Kelvin is: {temp} K")
    return ans
def ktof(temp):
    temp = round(5/9 * (temp - 32) + 273, 2)
    ans = print(f"The temperature in Fahrenheit is: {temp} F")
    return ans
   
while True:
 print()
 print("""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""")
 print("**** TEMPERATURE CONVATION (CELSIUS, KEVIN,FAHRENHEIT ) *****")
 print("""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""")
 print()
 print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
 print("Please select the option for temperature conversion")
 print(".............................................................")
 print("option 1: Celsius to Kelvin")
 print("option 2: kelvin to celsius")
 print("option 3: Celsius to Fahrenheit")
 print("option 4: Fahrenheit to Celsius")
 print("option 5: Fahrenheit to Kelvin")
 print("option 6: kelvin to fahrenheit")
    
 unit = input("Enter you option: ")
 temp = float(input("enter the temparature: "))

 if unit =='1':
  print("Celsius to Kelvin")
  ktoc(temp)
 elif unit =='2':
    print("kelvin to celsius")
    ctok(temp)
 elif unit =='3':
    print("Celsius to Fahrenheit")
    ctof(temp)
 elif unit =='4':
    print("Fahrenheit to Celsius")
    ftoc(temp)
 elif unit =='5':
    print("Fahrenheit to Kelvin")
    ftok(temp)
 elif unit =='6':
  print("option 6: kelvin to fahrenheit")
  ktof(temp)
 else:
    print(f"{unit} is an invalid option please try again")
 another = input("Do you want to convert another temperature? (yes/no): ").strip().lower()
 if another != 'yes':
   break

print()
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("################# THANK YOU FOR USING OUR SYSTEM #################")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
