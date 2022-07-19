from car import Car

class CarManager:
    
    def __init__(self):
        self.cars = []
        
        
    def createCars(self):
        car = Car()
        self.cars.append(car)