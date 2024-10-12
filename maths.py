import math

#area of a circle

def circumference():#2pieR
    r = float(input("Enter the radius: "))
    unit = input("imput unit: ")
    circm = float(2 * math.pi * r)
    ans = print(f"The circumference of the given circle is {circm} {unit}")
    return ans
def area_cicle():
    r = float(input("Enter the radius: "))
    unit = input("imput unit: ")
    area = float(math.pi * r **2)
    ans = print(f"The Area of the given circle is {area} {unit}2")
    return ans
def parimeter_sqr():
    s = float(input("Enter the lenth of side: "))
    unit = input("imput unit: ")
    peri = float(4*s)
    ans = print(f"The paremeter of the given squre is {peri} {unit}")
    return ans
def area_sqr():
    s = float(input("Enter the lenth of side: "))
    unit = input("imput unit: ")
    area = float(s **2)
    ans = print(f"The area of the given squre is {area} {unit}2")
    return ans
def parimeter_rec():
    L = float(input("Enter the length: "))
    w = float(input("Enter the width: "))
    unit = input("imput unit: ")
    peri = float(2 * (L + w))
    ans = print(f"The paremeter of the given Rectangle is {peri} {unit}")
    return ans
def area_rec():
    L = float(input("Enter the length: "))
    w = float(input("Enter the width: "))
    unit = input("imput unit: ")
    area = float(L * w)
    ans = print(f"The Area of the given Rectangle is {area} {unit}2")
    return ans
def parimeter_triangle():
    L = float(input("Enter the length: "))
    w = float(input("Enter the width: "))
    unit = input("imput unit: ")
    area = float((L * w) /2)
    ans = print(f"The Area of the given Rectangle is {area} {unit}")
    return ans
def area_triangle():
    L = float(input("Enter the base (enter 0 if not given): "))
    w = float(input("Enter the height (enter 0 if not given): "))
    h = float(input("Enter the hypotenuse (enter 0 if not given): "))
    unit = input("Input unit: ")

    if L == 0 and w == 0:
        print("Base and height cannot both be zero.")
        return None

    if L == 0:  # Base is unknown, calculate it using the hypotenuse and height
        L = math.sqrt(h**2 - w**2)

    if w == 0:  # Height is unknown, calculate it using the hypotenuse and base
        w = math.sqrt(h**2 - L**2)

    # Calculate area using the formula for area of a triangle
    area = 0.5 * L * w
    print(f"The area of the given triangle is {area} {unit}2")

def serface_area():
    L = float(input("Enter the length: "))
    w = float(input("Enter the width: "))
    h = float(input("Enter the width: "))
    unit = input("imput unit: ")
    area = float(2* (L * w) +2 * (L * h) +2* (h * w))
    ans = print(f"The Surface Area of the given cuboid or cube is {area} {unit}2")
    return ans
def volume_area():
    L = float(input("Enter the length: "))
    w = float(input("Enter the width: "))
    h = float(input("Enter the height: "))
    unit = input("imput unit: ")
    volume = float(L * w * h)
    ans = print(f"The volume of the given cuboid or cube is {volume} {unit}3")
    return ans
def serface_cylinder():
    r = float(input("Enter the radius: "))
    h = float(input("Enter the height: "))
    unit = input("imput unit: ")
    area = float(2* (math.pi * r **2) + (math.pi * 2* r *h))
    ans = print(f"The Surface Area of the given cylinder is {area} {unit}2")
    return ans
def volume_cylinder():
    r = float(input("Enter the radius: "))
    h = float(input("Enter the height: "))
    unit = input("imput unit: ")
    area = float(h * (math.pi * r **2))
    ans = print(f"The Surface Area of the given cylinder is {area} {unit}2")
    return ans

while True:

 print()
 print("===============================================================")
 print("******** AREA, PERIMETER AND VOLUME OF SHAPES *****************")
 print("===============================================================")
 print()
 print("enter 1 for a circumference of a circle: ")
 print("enter 2 for a area of a circle: ")
 print("enter 3 for a area of a squre: ")
 print("enter 4 for a perimeter of a squre: ")
 print("enter 5 for a perimeter of a rectagle")
 print("enter 6 for a area of a rectangle")
 print("enter 7 for a perimeter of a triangle")
 print("enter 8 for a area of a triangle")
 print("enter 9 for a surface area of a cuboid or a cube")
 print("enter 10 for a volume of a cuboid or a cube")
 print("enter 11 for a sirface area of a cylinder")
 print("enter 12 for a volume of a cylinder")
 print()
 print()
 print("----------------------------------------------------------------")
 choice = input("enter you choice: ")
 print("_________________________________________________________________")
 if choice =='1':
  print("------Perimeter of a circle----")
  circumference()
 elif choice =='2':
  print("------Area of a circle----")
  area_cicle()
 elif choice =='3':
  print("------Perimeter of squre----")
  parimeter_sqr()
 elif choice =='4':
  print("------Area of squre----")
  area_sqr()
 elif choice =='5':
  print("------Perimeter of a rectangle----")
  parimeter_rec()
 elif choice =='6':
  print("------Area of a rectangle----")
  area_rec()
 elif choice =='7':
  print("------perimeter of a triangle----")
  parimeter_triangle()
 elif choice =='8':
  print("------area of triangle----")
  area_triangle()
 elif choice =='9':
   print("------surface of cuboid/cube----")
   serface_area()
 elif choice =='10':
    print("------Volume of cuboid/cube----")
    volume_area()
 elif choice =='11':
  print("------surface area of cylinder----")
  serface_cylinder()
 elif choice =='12':
   print("------Volume of cylinder----")
   volume_cylinder()
 else:
   print("please enter valid choice")
   
 another = input("Do you want to calculate the area of another triangle? (yes/no): ").strip().lower()
 if another != 'yes':
   break

print()
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("################# THANK YOU FOR USING OUR SYSTEM #################")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")