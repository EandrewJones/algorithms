'''
Linear Search
-------------
An example of finding the maximum value in an array via
linear search.

Run time: O(n) 
'''
import time
from numpy import random

def lin_search_maximum(array: list) -> float:
    # Instantiate first item to max
    max_val = array[0]

    # Search one-by-one for max
    for num in array:
        if num > max_val:
            max_val = num
    return max_val

array_len = 100
double_array = random.randint(100, size=(array_len))

start_time = time.time()
max_val = lin_search_maximum(double_array)
run_time = time.time() - start_time

print('The max value is {} and linear search took {} ms \
to run for array of length {}.'.format(max_val, round(run_time, 3), array_len))
