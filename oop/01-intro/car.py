
class Car:
    def __init__(self, engine, color):
        self.engine = engine
        self.color = color

    def display(self):
        print(self.engine, self.color)

    def __str__(self):
        return str(self.engine) + " " + self.color


a = Car(1200, 'Blue')
b = Car(1000, 'White')
a.display()
b.display()
print(a)
print(b)
a.color = "Red"
print(a)