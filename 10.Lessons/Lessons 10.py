# # Винятки. Обробка Винятків. Попередження.
# # Except - Виняток, Помлка.
# # Вся структура називаєтсья Капсула.
# try:
#     try:
#         print("Start Code")
#     except SyntaxError:
#         print("We have SyntaxError")
# except NameError as error:
#     print(error)
# else: # Якщо немає помилок.
#     print("No problems")
# finally: # Виконується на кінці.
#     print("Finnaly Code")
# # Кожну капсулу " Структуру " можна огорнути ще додатковою капсулою.

# # Генерація винятків.
# raise - примусово генеруэ виняток

def checker(a):
    if type(a) != str:
        raise TypeError(f"Sorry, i can`t work with {type(a)}, we need class str")
    else:
        print("Good")

b = input("Enter your age ")
checker(b)

def checker(c):
    if type(c) != int:
        raise TypeError(f"Sorry, i can`t work with {type(c)}, we need class int")
    else:
        print("Good")

d = input("Enter you name ")
checker(d)



# Попередження - warnings
# Генерувати сповіщення можна за допомогою функції warn()
# import warnings


# warnings.simplefilter("ignore", SyntaxWarning)
# warnings.simplefilter("always",ImportWarning)

# warnings.warn("Warning, no code here", SyntaxWarning)



# try:
#     warnings.warn("Warning, library mot import", ImportWarning)
# except:
#     print("Warning process!")


