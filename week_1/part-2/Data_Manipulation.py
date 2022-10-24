def count(input): 
    # your code here 

    result = {}

    key_list = list(dict.fromkeys(input))
    for i in key_list:
        count = input.count(i)
        result.update({i:count})

    return result

input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x'] 
print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1} 

def group_by_key(input): 
    # your code here

    result = {}

    for i in input:
        if i['key'] in result.keys():
            value = result[i['key']] + i['value']
            result.update({i['key']:value})
        else:
            result.update({i['key']:i['value']})
            
    return result

input2 = [ 
     {'key': 'a', 'value': 3}, 
     {'key': 'b', 'value': 1}, 
     {'key': 'c', 'value': 2}, 
     {'key': 'a', 'value': 3}, 
     {'key': 'c', 'value': 5} 
] 
print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}