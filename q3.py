class Cat:
    """a cat"""
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"a Cat named {self.name}"
    def speak(self):
        print(f"{self.name} says meow!")

ella = Cat("Ella")
ella.speak()



class Dog:
    """a dog"""
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"a Dog named {self.name}"
    def speak(self):
        print(f"{self.name} says Woof!")

print(ella)
lexi = Dog("Lexi")
print(lexi)
lexi.speak()