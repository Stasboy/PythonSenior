# Перший код.
from cgitb import text
import string


print("Hello World!")

first = 23
print(first)

second = "Number"
print(second)
#--------------

print (first, second)
# Як проводити операції над числами.

a = 10 + 5
b = a + 20
c = ( a + b ) * 2
print(a,b,c)


# Робота з рядками.

# 1.Імя змінної не може містити в собі пробіли.
# 2. Імя змінної не може починатися з числа.
# 3. Регістер для змінних важливий, тобто є різниця між Var і Var.

first_string = "Hello world!"
third_string = """Hello world!"""

#Під час створення Рядка, враховуються тільки перші лапки
name =  input("Ваше Імя?")
#greeting переводиться як привітання
#Для того щоб поэднати дві змінні в одну (одного типу) використовуємо +
greeting = "Привіт," + name

print(greeting)

string = input("Напишіть будь-який текст: ")

string_length = len(string)

print(string_length)

result = 10 + 15

text = "Результат = " + str(result)
print(text)



result_2 = "10" + "15"
text_2 = "Результат = " + result_2
print(text_2)

a_2 = input("Перше число: ")
b_2 = input("Друге число: ")

result_3 = int(a_2) + int(b_2)

text_3 = "4) Результат = " + str(result_3)
print(text_3)