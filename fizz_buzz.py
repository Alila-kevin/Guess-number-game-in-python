def fizz_buzz(n):
    if n % 3==0 and n % 5 == 0:
        return "Fizz_ Buzz"
    if n % 3==0:
        return "Fizz"
    if n % 5==0:
        return "Buzz"

    return n
        
cf= int(input("enter the number: "))

print(fizz_buzz(cf))