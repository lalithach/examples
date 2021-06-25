# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 14:29:51 2021

@author: lalithac
"""

numbers = [45, 22, 14, 65, 97, 72]

# Always good to use enumerate over range whenever 
# contents of list are to be changed
for i,number in enumerate(numbers):
    if number % 5 == 0 and number % 3 == 0:
        numbers[i] = "FIZZBUZZ"
    elif number % 3 == 0:
        numbers[i] = "FIZZ"
    elif number % 5 == 0:
        numbers[i] = "BUZZ"
        
print(numbers)
# ['FIZZBUZZ', 22, 14, 'BUZZ', 97, 'FIZZ']
