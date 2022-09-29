# Week 1 Part 1

## Learning Git, GitHub & Python Basic

* [GitHub Training & Guides](https://www.youtube.com/watch?v=FyfwLX4HAxM&list=PLg7s6cbtAD15G8lNyoaYDuKZSKyJrgwB-&index=1) (Video)
* [Try git](https://try.github.io)
* [GitHub Guides](https://guides.github.com)
* [Python Basics](https://teamtreehouse.com/library/python-basics-3)

## Before assignment

From now on, we're going to start the project `stylish_automation_test`.

1. Fork this repository in AppWorks School account to your GitHub account.
2. You will get a `forked repository` in your GitHub account.
3. We call this repository in AppWorks School `upstream repository`.
4. Clone your `forked repository` from GitHub to your local machine.
5. Create a `develop` branch from `master` branch in your local machine.
6. Change your current branch from `master` to `develop` in your local machine.

## Assignment 1: Using GitHub

Every time before you start a new assignment, please create a new **assignment branch** from the **develop** branch with the following rules and complete the assignment on that branch.

```
Assignment branch naming rules:

  week_(week number)_part_(part number)

Ex: For week 1 part 1

  => week_1_part_1
```

1. Find a sub-folder named **Stylish** under the **students/[your_name]** folder.
2. Modify **README.md** file, write down **your name** in this file.
3. Make your first commit for the changes using git.
4. Push **current assignment branch** to `your forked repository`.

### How to hand-in?
Please find the **assignment branch** on your `forked repository` and make a pull request from this branch to `[your_name]_develop` of the `upstream repository`. (Please never make a pull request to the master branch of the `upstream repository`)

### About Pull Request
- Always include **short description of what you have done** in the description of pull request.

### Fix Issues
- You should check your email for tracking the status of pull request.
- If your pull request is not accepted, it means that the assignment have issues should be fixed. I will mention the issues in the comment.
- Fix issues, push new commits to your repository again. The pull request will automatically update itself, so you don't have to create another pull request for the same assignment.

### Sync Develop Branch
- If your pull request is merged, you should update local `develop` branch by pulling from remote `[your_name]-develop` branch.

## Assignment 2: Python Basic - BMI Calculator
Your job is to complete the following function

- check_bmi(): calculate the BMI value, and return True if BMI between 18.5 and 24. Otherwise, return False 

Formula: BMI = Weight(kg) / height<sup>2</sup> (m)

```python
def check_bmi(height, weight):
    # your code here

print(check_bmi(1.6, 60))   # print True
print(check_bmi(1.6, 40))   # print False
print(check_bmi(1.6, 100))  # print False
```


## Assignment 3: Python Basic - Find Maximum and Position
Your job is to complete the following two functions. 
1. find_max(): find the max value of an array of numbers.
2. find_position(): find the first position of the target number inside an array of numbers. The position should be counted starting from 0, if you can't find the target, please return -1.
* Reminder: you cannot use those built-in functions like max() and index() to complete this  assignment, please implement it by yourself. 

```python
def find_max(numbers): 
    # your code here

def find_position(numbers, target): 
    # your code here 

print(find_max([1, 2, 4, 5]) ) 	            # should print 5 
print(find_max([5, 2, 7, 1, 6]) )           # should print 7 
print(find_position([5, 2, 7, 1, 6], 5))    # should print 0 
print(find_position([5, 2, 7, 1, 6], 7))    # should print 2 
print(find_position([5, 2, 7, 7, 7, 1, 6], 7))  # should print 2 (the first one) print(find_position([5, 2, 7, 1, 6], 8)) # should print -1
```

## Assignment 4: Python Basic - Sum of Factorials  (Advanced Optional) 

Write a script to find the sum of factorials. (I.e. 1! + 2! + 3! … = ?)  

```python
def find_sum_of_factorials(numbers): 
    # your code here 

print(find_sum_of_factorials(3))  # = 1! + 2! + 3!, =  1 + 1 x 2 + 1 x 2 x 3,  should print 9
print(find_sum_of_factorials(1))  # should print 1
print(find_sum_of_factorials(5))  # should print 153
```

* Reminder: you cannot use those built-in functions like factorial() to complete this  assignment, please implement it by yourself.