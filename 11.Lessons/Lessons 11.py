# Ітератор

# for i in range(5):
#     print(i)

# my_list = [1,2,3]
# iterator = iter(my_list)
# for i in iterator:
#     print(i)

# for i in iterator:
#     print(i)

# class Counter:
#     def __init__(self,max_number):
#         self.i = 0
#         self.max_number = max_number

#     def __iter__(self):
#         self.i = 0
#         return self
    
#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#         return self.i

# count = Counter(6)

# for i in count:
#     print(i)

# Ліниве обчислення.

# Генератори.

# def raise_to_the_degrees(number,max_degree):
#     i = 0
#     while True:
#         yield number**i
#         i+=1

# res = raise_to_the_degrees(134,1435)
# print(str(res) + "\n")

# for _ in res:
#     print(str(_) + "\n" )

# class Helper:
#     def __init__(self,work):
#         self.work = work

#     def __call__(self,work):
#         return f"I will help you with your {self.work}. Afterwards i will help you with {work}."

# helper = Helper("homework")
# print(helper("cleaning"))
def checker(*exc_types):
    def checker(function):
        def checker(*args,**kwards):
            try:
                result = function(*args,**kwards)
            except Exception as exc:
                print(f"We have problems {exc}")
            else:
                print(f"No problems. Result = {result}")

@checker(NameError, TypeError, SyntaxError)
def calculate(expression):
    return expression*2

print (calculate(2))