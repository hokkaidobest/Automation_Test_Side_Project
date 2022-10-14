# Week 2 Part 1 (Deadline: 2022/10/26 23:59)

## Online Learning Material
* [HeadSpin University 課程](https://ui.headspin.io/university/learn/appium-selenium-fundamentals-2020/units)
  * Section 3: Python For Testing (Section 3.7 - 3.10)

## Assignment 1: Class and Object (Python)
Write a program which creates a class "Student" with the following Data:
student_name, mark1, mark2, mark3, total_marks

Methods:
1. set_student_details(): which sets the values to all the data except total_marks.
2. calculate_total(): which calculate the total_marks
3. display_student_details(): which display the student name and total marks.

Try to complete the following program.

```python
class Student:
    # your code here

student_a = Student()
student_a.set_student_details("Mary", 50, 60, 70)
student_a.caculate_total() # should print 180
student_a.display_student_details() # should print "Mary: 180"
```

## Assignment 2: Object-Oriented Programming (Python)

- Write a class called Animal is designed to model an animal. 
  - It contains an instance variables **sound** and two methods **get_sound()** and **get_type()**.
  - get_type(): print out "I am animal."
  - get_sound(): print out "Hello World"
- Write two subclasses of Animal called Dog and Cat.
  - Dog class:
    - override the method get_sound(). The Sound of Dog is "Woof! Woof!"
    - contains a method catch_cat(): print out "I caught a cat."
  - Cat class:
    - override the method get_sound(). The sound of cat is "Meow! Meow!"
    - contains a method catch_mouse(): print out "I caught a mouse."

Try to complete the following program.

```python
class Animal:
    # your code here

class Dog(Animal):
    # your code here

class Cat(Animal):
    # your code here

dog = Dog()
dog.get_type()  # Print "I am animal"
dog.get_sound() # Print "Woof! Woof!"
dog.catch_cat() # Print "I caught a cat."

cat = Cat()
cat.get_type()  # Print "I am animal" 
cat.get_sound() # Print "Meow! Meow!"
dog.catch_mouse() # Print "I caught a mouse."

```

## Assignment 3: Algorithm Practice (Advanced Optional)
Given a list of integers, return indices of the two numbers such that they add up to a
specific target. You may assume that each input would have exactly one solution, and you
may not use the same element twice.

```python
def two_sum(nums, target):
    # your code here

print(two_sum([2, 7, 11, 15], 9)) # Should be [0, 1], because nums[0] + nums[1] = 9
print(two_sum([3, 6, 11, 15], 17)) # Should be [1, 2], because nums[1] + nums[2] = 17
```