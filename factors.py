# -*- coding: utf-8 -*-
def factors(number):
    # ==============
    # Your code here
    factors1 = []
    for i in range (1, number-1): 
        if number % i == 0:
            if i != 1: 
                factors1.append(i)
    return factors1
            
    
    # ==============

print(factors(15)) # Should print [3, 5] to the console
print(factors(12)) # Should print [2, 3, 4, 6] to the console
print(factors(13)) # Should print “[]” (an empty list) to the console