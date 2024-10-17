# count = 0
# for x in range(1, 10):
#   if x % 2!=0:
#     continue
#   else:
#     count += 1
#     print(x)
  
# print(f"We have {count} even numbers")

#dictionary

capital = {"uganda": "kampala", "kenya": "Narobi", "Tanzania": "Dar-er-salaam"}

print(capital.get("uganda"))
print(capital)

capital.update({"ruanda": "kigali"})
print(capital)
#reove
# capital.pop("uganda")
# print(capital)
# capital.popitem()
# print(capital)

key = capital.keys()
print(key)
value = capital.values()
print(value)

for key, value in capital.items():
  print(f"The capital of {key} is {value}")