# # count = 0
# # for x in range(1, 10):
# #   if x % 2!=0:
# #     continue
# #   else:
# #     count += 1
# #     print(x)
  
# # print(f"We have {count} even numbers")

# #dictionary

# capital = {"uganda": "kampala", "kenya": "Narobi", "Tanzania": "Dar-er-salaam"}

# print(capital.get("uganda"))
# print(capital)

# capital.update({"ruanda": "kigali"})
# print(capital)
# #reove
# # capital.pop("uganda")
# # print(capital)
# # capital.popitem()
# # print(capital)

# key = capital.keys()
# print(key)
# value = capital.values()
# print(value)

# for key, value in capital.items():
#   print(f"The capital of {key} is {value}")

#decoretors
def othernames(func):
    def wrapper(name):
        print("Ali")
        func(name)
    return wrapper
@othernames
def name(name):
    print(name)

name("james")
def another_loc(func):
    def wrapper(loc):
        print("Church")
        func(loc)
    return wrapper
@another_loc
def location(loc):
    print(f"We will go to the {loc} on friday night")

location("Party")

#lambda function

maxnumber = lambda x, y: x if x > y else y
print(maxnumber(3765664, 6473673737))

minnumber = lambda x, y: x if x < y else y
print(minnumber(3765664, 6473673737))