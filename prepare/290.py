
class Car:
    def __init__(self, tire, price):
        self.tire = tire
        self.price = price


class Bike(Car):
    pass
    # def __init__(self, tire, price):
    #     self.tire = tire
    #     self.price = price
        
bicycle = Bike(2,100)

print(bicycle)
print(bicycle.price)