# calculater
#ask the user to input the oparater
opa = input("please enter the oparaters +, -, %, *, /: ")

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
    print("invalid oparetor please look and try again")