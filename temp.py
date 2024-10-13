#Celsius to Kelvin + 273.15
#kelvin to celsius -  273.15

unit = input("I this temparature in Celsius or Kelvin (C/K): ").upper()
temp = float(input("enter the temparature: "))

if unit =='C':
    temp = round(temp + 273.15, 2)
    print(f"The temperature in Kelvin is: {temp} K")
elif unit =='K':
    temp = round(temp - 273.15, 2)
    print(f"The temperature in Celcius is: {temp} C")
else:
    print(f"{unit} is an invalid unit of measure")
