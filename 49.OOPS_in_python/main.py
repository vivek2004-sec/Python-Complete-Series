class Dog:
    def sound(self):
        print("Woof!")

class Cat:
    def sound(self):
        print("Meow!")

class Cow:
    def sound(self):
        print("Moo!")

# Same method name → different behavior!
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()