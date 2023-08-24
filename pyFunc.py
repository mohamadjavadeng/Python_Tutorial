def FirstFunc():
    print("hello world")


def Func1():
    x = "This is x"
    print(x)

def Func2(x):
    print(f'this is {x}')

def Func3(x, y):
    print(x, " ", y)

def Func4(x, y=10):
    print(x, " ", y)
FirstFunc()
Func1()
Func2(3)
Func2("\"I am a string\"")
Func3(1, 15)
Func3(y=10, x="Hi")
Func4(12)
Func4(y="Bye", x=13)
# _________________________________________
def FunctionArg(*Kids):
    for i in range(len(Kids)):
        print(f'Your {i}th arg is {Kids[i]}')
FunctionArg(10, "Donya", 26.3)

def FunctionKeyWord(**keywords):
    total_name = keywords["firstname"] + keywords["lastname"]
    print(f'your total name is {total_name}')

FunctionKeyWord(firstname = "mohammadjavad", lastname="Arab")
#_______________________________________
def FunctionList(inputx):
    for x in inputx:
        print(x, end=",")
y = ["a", "b", "c", "d"]
FunctionList(y)

def FunctionAdder(x = 0):
    return x + 1

print(FunctionAdder(10))
print(FunctionAdder(11))
print(FunctionAdder(26))
print(FunctionAdder())

# recursive function
def Adder(x):
    if x != 1:
        sum = x + Adder(x - 1)
    else:
        return 1
    return sum
print(Adder(6))
