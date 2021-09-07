def maximum(value1, value2, value3):
  
    if (value1 >= value2) and (value1 >= value3):
        biggest = value1
  
    elif (value2 >= value1) and (value2 >= value3):
        biggest = value2
    else:
        biggest = value3
          
    return biggest
   
value1 = 12
value2 = 27
value3 = 36
print('biggest =', maximum(value1, value2, value3))

def minimum(value4, value5, value6, value7):
  
    if (value4 <= value5) and (value4 <= value6) and (value4 <= value7):
        smallest = value4
  
    elif (value5 <= value1) and (value5 <= value6) and (value5 <= value6):
        smallest = value5
    
    elif (value6 <= value4) and (value6 <= value5) and (value6 <= value7):
        smallest = value5
    else:
        smallest = value7
          
    return smallest
   
value4 = 15
value5 = 9
value6 = 27
value7 = 14
print('smallest =', minimum(value4, value5, value6, value7))
