# Week 1 Part 2 (Deadline: 2022/10/23 23:59)

## Online Learning Material
* [List & Tuple](https://www.youtube.com/watch?v=JLU5oc4_VtA&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=4)
* [Set & Dictionary](https://www.youtube.com/watch?v=L3-KuGYhw78&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=5)

## Assignment 1: List and Dictionary (Python)
Complete the function below which can calculate the average price of all products. 

```python
def avg(data): 
    # your code here

print( 
    avg({ 
        "products": [ 
              { 
                     "name": "Product 1", 
                     "price": 100 
               }, 
              { 
                     "name": "Product 2", 
                     "price": 700 
               }, 
              { 
                     "name": "Product 3", 
                     "price": 300 
               } 
       ] 
   }) 
) 
# print the average price of all products (round to 3 decimal)
```

## Assignment 2: Data Manipulation (Python) 
Complete the following functions 

1. count(): return an object which shows the count of each character.
2. group_by_key(): return an object which shows the summed up value of each key. 

Note:
- The input format is different for these two functions. 
- In the second function, the input may have the same key but different values, the output  should have each key only once. 

```python
def count(input): 
    # your code here 

input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x'] 
print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1} 


def group_by_key(input): 
    # your code here

input2 = [ 
     {'key': 'a', 'value': 3}, 
     {'key': 'b', 'value': 1}, 
     {'key': 'c', 'value': 2}, 
     {'key': 'a', 'value': 3}, 
     {'key': 'c', 'value': 5} 
] 
print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}
```

## Assignment 3: Algorithm Practice (Advanced Optional) 
We created a function in Assignment 3 in week 1 part 1 which can find the position of the target number  inside an array of numbers. 

Actually, if the array was Sorted already, there is a beautiful algorithm called **Binary Search** which can do this job efficiently. 

You can try to look up these keywords and learn the concept behind this algorithm and write the code by yourself. 

For simplicity, you can assume that there are no duplicate numbers in the given array. It  could be a bit of a challenge if you haven’t learned any algorithm.

```python
def binary_search_position(numbers, target): 
    # your code here 

print(binary_search_position([1, 2, 5, 6, 7], 1)) # should print 0 
print(binary_search_position([1, 2, 5, 6, 7], 6)) # should print 3
```


