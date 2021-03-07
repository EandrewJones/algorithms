'''
Checking whether a word is a palindrome

A palindrome is a word that reads the same in both directions.

Punctuation, spaces, and apostrophes are usually ignored.

This algorithm will confirm whether the input is a palindrome.

Examples:
1. radar
2. madam
3. Was it a car or a cat I saw?
'''

def check_palindrome(string: str) -> bool:
    # Remove special characters and spaces
    string = string.lower()
    string = [character for character in string 
              if character.isalnum()]
            
    # reverse and compare
    start_idx = 0
    end_idx = len(string) - 1
    
    while end_idx > start_idx:
        if string[start_idx] != string[end_idx]:
            return False
        start_idx += 1
        end_idx -= 1
        
    return True 

# We can also just use string slicing in python
# but this does not translate well to other languages
def check_palindrome_python(string: str) -> bool:
    # Remove special characters and spaces
    string = string.lower()
    string = [character for character in string 
              if character.isalnum()]
    
    # Compare with reverse
    if string == string[::-1]:
        return True
    else:
        return False
    

if __name__ == '__main__':
    
    palindromes = ['radar', 'madam' , 'Was it a car or a cat I saw?',
                   'parrot', "This isn't a palindrome!"]
    checks = [check_palindrome(p) for p in palindromes]
    
    for p, c in zip(palindromes, checks):
        print('{} is a palindrome: {}'.format(p, str(c)))
        
    
