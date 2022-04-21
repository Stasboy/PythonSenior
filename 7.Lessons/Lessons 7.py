class Human:
    def __init__(self,name):
        self.name = name

class Auto:
    def __init__(self,brand):
        self.brand = brand
        self.passangers = []

    def add_passenger(self,human):
        self.passangers.append(human)

    def print_passengers(self):
        if self.passangers != []:
            print(f"Names of {self.brand} passengers:")
            for i in self.passangers:
                print(i.name)
        else:
            print(f"There are not passenger in {self.brand}")

nick = Human("Nick")
kate = Human("Kate")

car = Auto("Volkswagen")
car.add_passenger(nick)
car.add_passenger(kate)

car.print_passengers()
