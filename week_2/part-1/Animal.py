class Animal:
    # your code here

    def __init__(self):
        self.sound = "Hello World"

    def get_type(self):
        print("I am animal.")

    def get_sound(self):
        print(self.sound)

class Dog(Animal):
    # your code here

    def __init__(self):
        self.sound = "Woof! Woof!"

    def get_sound(self):
        print(self.sound)

    def catch_cat(self):
        print("I caught a cat.")

class Cat(Animal):
    # your code here

    def __init__(self):
        self.sound = "Meow! Meow!"

    def get_sound(self):
        print(self.sound)

    def catch_mouse(self):
        print("I caught a mouse.")

dog = Dog()
dog.get_type()  # Print "I am animal"
dog.get_sound() # Print "Woof! Woof!"
dog.catch_cat() # Print "I caught a cat."

cat = Cat()
cat.get_type()  # Print "I am animal" 
cat.get_sound() # Print "Meow! Meow!"
cat.catch_mouse() # Print "I caught a mouse."