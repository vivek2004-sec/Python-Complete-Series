class Engine:
    def __init__(self):
        self.status = "running"

class Car:
    def __init__(self):
        self.engine = Engine()   # Car creates its own Engine internally

car = Car()
del car   # when car is destroyed, its engine goes with it — no external reference