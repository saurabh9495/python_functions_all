class Car:
    def __init__(self):
        print('Car initialises with ',self)

class SubCar(Car):
    def __init__(self):
        Car.__init__('testing')

print(issubclass(SubCar, Car))
# True