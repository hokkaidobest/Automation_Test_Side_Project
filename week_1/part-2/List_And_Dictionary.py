def avg(data): 
    # your code here

    sum = 0
    for x in data['products']:
        sum = sum + x['price']
    
    result = sum / len(data['products'])
    return round(result, 3)

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