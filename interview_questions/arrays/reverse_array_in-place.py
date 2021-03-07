'''
Reversing an array in-place

We want to reverse an array A[] in O(N) linear time complexity
and the algorithm must be in-place such that no additional memory
is used.

Example:

input: [1,2,3,4,5]
output: [5,4,3,2,1]
'''

def reverse(array: list) -> list:
    # instantiate indices
    start_idx = 0
    end_idx = len(array) - 1
    
    while end_idx > start_idx:
        # Swap items
        array[start_idx], array[end_idx] = array[end_idx], array[start_idx]
        
        # Update indices
        start_idx += 1
        end_idx -= 1

    return array

if __name__ == '__main__':
    
    a = [1,2,3,4,5]
    b = reverse(a.copy())
    print('Array: {}\nReversed array: {}'.format(a, b))
    