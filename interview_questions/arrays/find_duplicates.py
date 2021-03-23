'''
How to find duplicate items in an array.

We want to find duplicates in a one-dimensional array 
of integers in O(n) time where the values of the integer
are less than the length of the array.

Example:

In array [1, 2, 3, 1, 5], the algorithm would identify 1 as 
a duplicate.

Note:
This algorithm cannot handle values < 0 or values greater than
the length of the array.
'''

def find_duplicates(array: list) -> list:
    duplicates = []
    for item in array:
        if array[abs(item)] >= 0:
            array[abs(item)] = -array[abs(item)]
        else:
            duplicates.append(abs(item))
    
    return duplicates

if __name__ == '__main__':
    A = [1, 2, 3, 1, 4, 2, 5]
    duplicates = find_duplicates(A)
    print('Duplicated values in the array are {}.'.format(duplicates))
            