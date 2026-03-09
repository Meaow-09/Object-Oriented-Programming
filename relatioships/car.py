class Engine:
    def __init__(self, type, horsepower):
        self.type = type
        self.horsepower = horsepower

    def __str__(self):
        return f"Engine(type={self.type}, horsepower={self.horsepower})"

class Car:
    def __init__(self, make, model, year, engine):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine  # Car HAS-A Engine
        self.passengers = []  # Car HAS-A list of Passengers

    def __str__(self):
        return f"Car(make={self.make}, moddefel={self.model}, year={self.year}, engine={self.engine})"

    def add_passenger(self, passenger):
        print(f"{passenger._name} has been added to the {self.make} {self.model}.")
        self.passengers.append(passenger)

    def remove_passenger(self, passenger):
        print(f"{passenger._name} has been removed from the {self.make} {self.model}.")
        self.passengers.remove(passenger)

class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Passenger(name={self.name}, age={self.age})"

    def board_car(self, car):
        print(f"{self.name} boards the {car.make} {car.model}.")
        car.add_passenger(self)

    def leave_car(self, car):
        print(f"{self.name} leaves the {car.make} {car.model}.")
        car.remove_passenger(self)

if __name__ == "__main__":
    # Create an Engine instance
    my_engine = Engine(type="V8", horsepower=450)

    # Create a Car instance with the Engine
    my_car = Car(make="Ford", model="Mustang", year=2021, engine=my_engine)

    # Print the Car details
    print(my_car)
    print("Car's Engine:", my_car.engine)

    # Create a Passenger instance
    passenger = Passenger(name="Alice", age=30)
    print(passenger)

    # Passenger boards the car
    passenger.board_car(my_car)