import array
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

#array
a = array.array('i', [2, 3, 5, 6, 10, 35])
print(len(a))# length of array
print(a[2])
print(a[-2])
print(a)

#adding element in the array
a.append(7)
print(a)
a.extend([45, 48, 52])
print(a)

a.insert(3, 67)
print(a)

#removing element in the array
a.pop(7)
print(a)
a.pop()
print(a)
a.remove(2)
print(a)
#adding array
b = array.array('i', [2,34, 45, 87, 100])
c = a + b
print(c)
#slicing array
c[4:5]
print(c[4:6])
print(c[4:-2])

print(c)
for x in c:
    print(x)
f =0
while f < c[4]:
    print(c[f])
    f+=1