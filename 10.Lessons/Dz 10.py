
def checker(a):
    if type(a) != int:
        raise TypeError(f"Sorry, i can`t work with {type(a)}, we need class int")
    else:
        print("Good")

b = input("Enter your age ")
checker(b)

def checker(c):
    if type(c) != str:
        raise TypeError(f"Sorry, i can`t work with {type(c)}, we need class str")
    else:
        print("Good")

d = input("Enter you name ")
checker(d)