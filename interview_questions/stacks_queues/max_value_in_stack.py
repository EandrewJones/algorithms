"""
Max value in stack

Find the item with the maximum value in a stack in O(1) running
time complexity. You may use O(N) memory.

The algorithm below uses an additional stack to track the current 
maximum value in the stack.
"""


class Stack:
    
    def __init__(self):
        self.stack = []
        self.max_value = []
        self.numeric_stack = []
        
    def __iter__(self):
        """
        >>> stack = Stack()
        >>> stack.push('a')
        >>> stack.push('b')
        >>> stack.push('c')
        >>> tuple(stack)
        ('a', 'b', 'c')
        """
        for item in self.stack:
            yield item
        
    def __len__(self):
        """
        >>> stack = Stack()
        >>> stack.push('a')
        >>> stack.push('b')
        >>> stack.push('c')
        >>> len(stack)
        3
        """
        return len(self.stack)
    
    def __str__(self):
        """
        >>> stack = Stack()
        >>> stack.push('a')
        >>> stack.push('b')
        >>> stack.push('c')
        >>> str(stack)
        'c > b > a'
        """
        return " > ".join(reversed([str(item) for item in self.stack]))
    
    # Append item to top of stack (end of list) // O(1)
    def push(self, data):
        self.stack.append(data)
        if isinstance(data, (int, float)):
            self.numeric_stack.append(data)
            if self.is_empty() or data >= max(self.numeric_stack): 
                self.max_value.append(data)
        
    # Remove top item of stack and return it // O(1)
    def pop(self):
        """
        >>> stack = Stack()
        >>> stack.pop()
        Traceback (most recent call last):
        ....
        IndexError: list index out of range
        >>> stack.push('b')
        >>> stack.push('a')
        >>> stack.pop()
        'a'
        >>> stack.pop()
        'b'
        """
        if self.is_empty():
            raise IndexError("list index out of range")
        data = self.stack[-1]
        if isinstance(data, (int, float)):
            del self.numeric_stack[-1]
            if data == self.max_value[-1]:
                del self.max_value[-1]
        del self.stack[-1]
        
        return data
    
    # Return last item without removing it
    def peek(self):
        """
        >>> stack = Stack()
        >>> stack.peek()
        Traceback (most recent call last):
        ....
        IndexError: list index out of range
        >>> stack.push('b')
        >>> stack.push('a')
        >>> stack.peek()
        'a'
        >>> stack.peek()
        'a'
        """
        if self.is_empty():
            raise IndexError("list index out of range")
        return self.stack[-1]
    
    def is_empty(self):
        """
        >>> stack = Stack()
        >>> stack.is_empty()
        True
        >>> stack.push('a')
        >>> stack.is_empty()
        False
        """
        return self.stack == []
    
    # Returns current max value of stack // O(1)
    def max(self):
        """
        >>> stack = Stack()
        >>> stack.max()
        Traceback (most recent call last):
        ....
        IndexError: list index out of range
        >>> stack.push('a')
        >>> stack.max()
        Traceback (most recent call last):
        ....
        TypeError: list contains no numeric items
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.max()
        2
        >>> stack.push(2)
        >>> stack.pop()
        2
        >>> stack.pop()
        2
        >>> stack.max()
        1
        """
        if self.is_empty():
            raise IndexError("list index out of range")
        if self.numeric_stack == []:
            raise TypeError("list contains no numeric items")
        return self.max_value[-1]
    
    
if __name__ == "__main__":
    from doctest import testmod
    
    testmod()