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
# while Loop
z = 1
while z in range(10):
    print(z)
    z = 2 * z

list1 = ["Donya", "Mohammadjavad", "leila", "rozi", "amir"]
while len(list1) > 2:
    list1.remove(list1[-1])

print(list1)

#for loop
list1 = ["Donya", "Mohammadjavad", "leila", "rozi", "amir"]
for i in range(10):
    print(i, end=',')
print()
for name in list1:
    print(name, end=',')