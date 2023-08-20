import numpy as np

x1 = 1
x2 = 2.3
x3 = "3"

x1int = int(x1)
x2int = int(x2)
x3int = int(x3)

print(x1int)
print(x2int)
print(x3int)

#---- String ----#
string1 = "hello"
print(len(string1))
print(string1[0])

#---- list ----#
list1 = ["Donya", "Mohammadjavad", "leila"]
print(len(list1))
print(len(list1[1]))
list1.append("Rozi")
list1.append("Amir")
print(list1[1:4])
list1.remove("leila")
print(list1)
#--- Tuple ---#
#update Tuple
x = ("apple", "banana", "cherry")
#x[1] = "cucumber"
#print(x)
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#----- Set ----#
thisset = {"apple", "banana", 1, "cherry", 5, 2}
print(thisset)
print("banana" in thisset)  # True

# add to set
thisset.add("orange")
print(thisset)

thatset = {1, 2, True, False}
print(thatset)

#---- dictionary ----#
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])
print(thisdict["model"])
print(thisdict["year"])
x = thisdict.keys()
print(x)
x = list(x)
print(x)
thisdict["year"] = 2015
thisdict["color"] = "red"
print(thisdict)
x = thisdict.keys()