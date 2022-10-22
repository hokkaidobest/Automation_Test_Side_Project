def count(input): 
    # your code here 

    result = {}

    key_list = list(dict.fromkeys(input))
    for x in key_list:
        count = input.count(x)
        result.update({x:count})
    return result

input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x'] 
print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1} 


# def group_by_key(input): 
#     # your code here

# input2 = [ 
#      {'key': 'a', 'value': 3}, 
#      {'key': 'b', 'value': 1}, 
#      {'key': 'c', 'value': 2}, 
#      {'key': 'a', 'value': 3}, 
#      {'key': 'c', 'value': 5} 
# ] 
# print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}