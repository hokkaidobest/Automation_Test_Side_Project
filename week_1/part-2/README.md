# Week 1 Part 2

## Assignment 1: Function, Array and Dictionary (Python)
Complete the function below by Python which can calculate the average price of all the  products. 

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
Complete the following functions by Python 

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



