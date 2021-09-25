'''
Example of a stack implementation

Notes
-----

Stacks are abstract data types with a LIFO - last in, first out - structure
'''


class Stack:

    def __init__(self):
        self.stack = []

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


def test_stack() -> None:
    """
    >>> test_stack()
    """
    stack = Stack()
    assert stack.is_empty() is True
    assert str(stack) == ""

    try:
        stack.pop()
        assert False # This should not happen
    except IndexError:
        assert True # This should happen

    try:
        stack.peek()
        assert False # This should not happen
    except IndexError:
        assert True # This should happen

    for i in range(10):
        assert len(stack) == i
        stack.push(i)
    assert str(stack) == ' > '.join(reversed([str(i) for i in range(10)]))

    assert stack.pop() == 9
    assert stack.peek() == 8
    assert stack.pop() == 8
    assert len(stack) == 8


if __name__ == "__main__":
    from doctest import testmod

    testmod()
