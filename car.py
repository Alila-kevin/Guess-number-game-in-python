class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def __str__(self):
        return f"The car is a {self.make} {self.model}, released in {self.year}, priced at Ksh. {self.price}"

class Dealer:
    def __init__(self, name):
        self.name = name
        self.cars = []
    
    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, identifier):
        # Remove car based on make or model
        self.cars = [car for car in self.cars if car.make != identifier and car.model != identifier]

    def list_cars(self):
        if not self.cars:
            print("No cars available.")
            return
        for car in self.cars:
            print(car)

def user_input():
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    year = input("Enter the year of release: ")
    price = input("Enter the price: ")
    
    return Car(make, model, year, price)

# Create a dealer
dealer = Dealer("Alila Motors")

# Add a car from user input
dealer.add_car(user_input())

# List all cars
dealer.list_cars()

def delete_car():
    how = input("Enter the model or make to delete: ")
    dealer.remove_car(how)

# Optionally, you can call delete_car to test the removal
delete_car()
dealer.list_cars()
