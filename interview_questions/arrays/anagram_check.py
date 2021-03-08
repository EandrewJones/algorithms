'''
How to check whether two words are anagrams.

An anagram is a word formed by rearranging the letters
from another word. Typically all letters are used and only once.

Examples:

sadder & dreads
listen & silent
'''

# This is a simple job for the set function
def is_anagram_python(word1: str, word2: str) -> bool:
    return set(word1) == set(word2)

# If this is not allowed, we'd have to do a manual check
def is_anagram(word1: str, word2: str) -> bool:
    # Check lengths first
    if len(word1) != len(word2):
        return False
    
    # sort and compare
    word1 = sorted(word1)
    word2 = sorted(word2)
    for a, b in zip(word1, word2):
        if a != b:
            return False
        
    return True

if __name__ == '__main__':
    
    words = ['silent', 'sadder', 'earth', 'pare']
    anagrams = ['listen', 'dreads', 'heart', 'pure']
    
    print('Pythonic check with set:\n')
    for a, b, in zip(words, anagrams):
        print('\t{} amd {} are anagrams: {}'.format(a, b, is_anagram_python(a, b)))
        
    print('\nGeneric check with sort and loop:\n')
    for a, b, in zip(words, anagrams):
        print('\t{} amd {} are anagrams: {}'.format(a, b, is_anagram(a, b)))