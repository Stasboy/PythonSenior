# def f (x):
#     return x * 2

# result = f(3)

# print (result)

# #Як передавати число з клавіатури в фунцію.

# z = f(int(input("Enter Number: ")))
# print(z) 

# # Як передати більш ніж один параметр в функцію.

# def k(a,b,c):
#     return a + b + c

# result = (int(input("Enter Number: ")), int(input("Enter Number: ")), int(input("Enter Number: ")))
# print(result)

# #------------------------------
# def num(x):
#     return x * 2

# z = num(3)

# if z > 5:
#     print( str(z) + "Більше 5")
# else:
#     print(str(z) + "Менше 5")

#------------------------------
def max(a,b):
    
    if a > b:
        return("Перше число більше " + str(a))
    else:
        return("Друге число більше " + str(b))

result = max(int(input("Перше число")),(int(input("Друге число"))))
print(result)
#--------------------
def lenght(string):
    string_lenght = lenght(string)

    return(string_lenght)
result = len(input("Введіть своє речення: "))
print(result)
#---------------------
a = input("Введіть перше число")
b = input("Введіть друге число")
c = input("Введіть третє число")

result = print((int(a) + int(b) + int(c)) / 3 )
print(result)
#---------------------
