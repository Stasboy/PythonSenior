# ----- Успадкування Основного класа. -----

# class Human:
#     height = 180
#     satiety = 50

# class Student(Human):
#     pass

# class Worker(Human):
#     satiety = 80


# nick = Student()
# stas = Worker()

# print(nick.satiety)
# print(stas.satiety)

# #Дочірні - класи які успадковані.
# # ----- Успадкування успадкованих класів -----

# class Grandparent:
#     height = 170
#     satiety = 100
#     age = 60

# class Parent(Grandparent):
#     age = 40

# class Child(Parent):
#     height = 150
#     def __init__(self):
#         print(self.height)
#         print(self.satiety)
#         print(self.age)

# nick = Child()

# ----- Функція super() -----

# class Hello:
#     def __init__(self):
#         print("Hello!")

# class Hello_World(Hello):
#     def __init__(self):
#         super().__init__()
#         print("World!")


# hi = Hello_World()


# ----- Множине успадкування -----

class Hero:
    def __init__(self):
        super().__init__()
        self.height = input("Enter the height of your hero ")
