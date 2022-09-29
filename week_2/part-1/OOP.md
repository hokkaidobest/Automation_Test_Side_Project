# Week 2 Part 1

## Assignment 1: Object-Oriented Program (Python)

- Write a class called Animal is designed to model an animal. 
  - It contains two instance variables **sound** and **food** and two methods **get_sound()** and **get_food()**.
- Write two subclasses of Animal called Dog and Cat.
  - The Sound of Dog is "Wow! Wow!" and the favorite food is "Bone"
  - The sound of cat is "Meow! Meow!" and the favorite food is "Fish" 

Try to complete the following program.

```python
class Animal:
    # your code here

class Dog(Animal):
    # your code here

class Cat(Animal):
    # your code here

dog = Dog()
dog.get_sound() # Print "Wow! Wow!"
dog.get_food()  # Print "Bone"

cat = Cat()
cat.get_sound() # Print "Meow! Meow!"
cat.get_food()  # Print "Fish"
```