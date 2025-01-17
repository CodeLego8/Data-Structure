class Car:
    def __init__(self, tire, price):
        self.tire = tire
        self.price = price

class CarInfo(Car):

    ABC = 3

    def __init__(self, information):
        self.information = information

    @staticmethod
    def process(sa,b):
         a = 1
         b = 2
         return a + b

a = Car(4,1000)
t = Car(3,999)
b = CarInfo("Bus")
b = CarInfo(t)

c = CarInfo(Car(1,1))


print(a.price, a.tire)
print(b.information)
print(t.price)
print(c)


