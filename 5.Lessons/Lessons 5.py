# import turtle
# a = turtle.Turtle()

# for i in range(4):
#     a.forward(50)
#     a.right(90)

# turtle.done()

class Hero:
    amount_students = 0
    def __init__(self, name, health, age, race, power): 
        self.name = name
        self.age = age
        self.health = health
        self.race = race
        self.power = power
        self.lvl = 1

    def show(self):
        print("Name: " + str(self.name))
        print("Health: " + str (self.health))
        print("Age: " + str (self.age))
        print("Race: " + str (self.race))
        print("Power: " + str (self.power))
        print("Level: " + str (self.lvl))
        return(First)

    def LvlUp(self):
        self.lvl +=1
        print("Lvl update for name: ")

First = Hero(name=(input("Enter name: ")), health=(int(input("Enter health: "))), age=(int(input("Enter age: "))), race=(input("Enter race: ")), power=(int(input("Enter power: ")))) 
Second = Hero(name=(input("Enter name: ")), health=(int(input("Enter health: "))), age=(int(input("Enter age: "))), race=(input("Enter race: ")), power=(int(input("Enter power: ")))) 
Third = Hero(name=(input("Enter name: ")), health=(int(input("Enter health: "))), age=(int(input("Enter age: "))), race=(input("Enter race: ")), power=(int(input("Enter power: ")))) 

First.show()
Second.show()
Third.show()
