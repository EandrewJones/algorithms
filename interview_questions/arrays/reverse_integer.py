'''
How to reverse an integer

Design an efficient algorithm to reverse a given integer.

Example:

input: 1234
output: 4321
'''

# Use the module operator to collect the last digit
# Then use integer division to delete the last digit
# build the new integer up tens-place by tens-place
def reverse_integer(n: int) -> int:
    reverse = 0
    remainder = 0
    
    while (n > 0):
        remainder = n % 10
        n = n // 10
        reverse = reverse * 10 + remainder
    return reverse

if __name__ == '__main__':
    print(reverse_integer(12345678))