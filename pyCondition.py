"""
-------------------------------------------
 if....elif....else
-------------------------------------------
"""
# if....elif....else
#-------------------------------------------
mylist = ["apple", "banana", "cherry"]
fruit = "banana"
if fruit in mylist:
    indexf = mylist.index(fruit)

print(indexf)

a = 1
b = 2
if a > b :
    print("a is greater than b")
else:
    print("a is greater than b")

a = 2
b = 2
if a > b :
    print("a is greater than b")
elif a < b :
    print("b is greater than a")
else:
    print("a is equal to b")

a, b, c = (10, 5, 3)
if a > b and a > c:
    print("a is the greatest parameter")
#------------------------------------
