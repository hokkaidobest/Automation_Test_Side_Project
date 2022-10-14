# Week 2 Part 2 (Deadline: 2022/10/30 23:59)

## Online Learning Material
* [Pandas DataFrame 匯出到 Excel](https://www.delftstack.com/zh-tw/howto/python-pandas/export-pandas-dataframe-to-excel-file/)
* [Python & Pandas](https://stylengineer.com/program/python-pandas/)

## Assignment 1: Excel Application

### Part 1
There is a score table of the English students.

| Student   | Reading | Listening | Speaking | Writing |
|-----------|---------|-----------|----------|---------|
| Student A | 80      | 75        | 88       | 80      |
| Student B | 88      | 86        | 90       | 95      |
| Student C | 92      | 85        | 92       | 98      |
| Student D | 81      | 88        | 80       | 82      |
| Student E | 75      | 80        | 78       | 80      |

Create a spreadsheet for the below score table using Python.

### Part 2

The below table presents the weights of different section of the score. 

| Section   | Weight |
|-----------|--------|
| Reading   | 20%    |
| Listening | 25%    |
| Speaking  | 30%    |
| Writing   | 25%    |

Write a Python script to read the value from spreadsheet, and calculate the **Weighted Average** for each student.

Expected Output:
```text
student: Student A, score: 81.15
student: Student B, score: 89.85
student: Student C, score: 91.75
student: Student D, score: 82.7
student: Student E, score: 78.4
```

## Assignment 2: Exception Handling

Complete the following functions by Python 

1. division(): return the result of division.
- Throw ZeroDivisionError if y is 0.
- Throw TypeError if y is not an integer.
- Whether an exception occurs or not, it will Print "---Finish---"

```python
def division(x, y):
    # your code here

division(100, 10)   # Should print 10.0 and "---Finish---"
division(100, 0)    # Should Throw ZeroDivisionError, print "y cannot be 0" and "---Finish---"
division(100, "a")  # Should Throw TypeError, print "y should be integer" and "---Finish---"

```

## Assignment 3: Algorithm Practice (Advanced Optional)
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

```python
def running_sum(nums):
    # your code here

print(running_sum([1, 2, 3, 4])) # Should be [1, 3, 6, 10] because [1, 1+2, 1+2+3, 1+2+3+4]
print(running_sum([1, 1, 1, 1, 1])) # Should be [1, 2, 3, 4, 5]
print(running_sum([3, 1, 2, 10, 1])) # Should be [3, 4, 6, 16, 17]
```