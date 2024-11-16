# calculater
#ask the user to input the operator
opa = input("please enter the operators between  +, -, %, *, /: ")

fd = float(input("input the first degit: "))
sd = float(input("input the second degit: "))

if opa == '+':
    print(fd +sd)
elif opa =='-':
    print(fd-sd)
elif opa =='%':
    print(fd%sd)
elif opa == '*':
    print(fd*sd)
elif opa =='/':
    print(fd/sd)
else:
    print("invalid operator please look and try again")
