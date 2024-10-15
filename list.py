# number =list(range(20))
# james, kili, mery, clinton, *other = number
# print(number)
# print(other)
# for index, numbers in enumerate(number):
#     print(index, numbers)
names = ["james", "george", "cherles", "willium", "jame", "christine"]
print(names)
#add append
names.append("john")
print(names)

names.insert(4, "jane")
print(names)

#remove
names.pop(0)
print(names)

names.remove("george")
print(names) 
del names[0:2]
print(names) 
names.clear()
print(names)  

#find 
#print(names.index("jame"))
print(names.count("jame"))
if "george" in names:
    print(names.index("george"))