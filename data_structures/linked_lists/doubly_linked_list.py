'''
Example of a doubly-linked list implementation
'''

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous_node = None
        
    def __str__(self):
        return f"{self.data}"
        
        
class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_of_nodes = 0
        
    def __iter__(self):
        """
        >>> linked_list = DoublyLinkedList()
        >>> linked_list.insert_start('b')
        >>> linked_list.insert_start('a')
        >>> linked_list.insert_end('c')
        >>> tuple(linked_list)
        ('a', 'b', 'c')
        """
        node = self.head
        while node:
            yield node.data
            node = node.next_node
    
    def __str__(self):
        """
        >>> linked_list = DoublyLinkedList()
        >>> linked_list.insert_end('a')
        >>> linked_list.insert_end('b')
        >>> linked_list.insert_end('c')
        >>> str(linked_list)
        'a->b->c'
        """
        return "->".join([str(item) for item in self])
        
    def __len__(self):
        """
        >>> linked_list = DoublyLinkedList()
        >>> for i in range(0, 10):
        ...     linked_list.insert_at_nth(i, i + 1)
        >>> len(linked_list) == 10
        True
        """
        return len(tuple(iter(self)))
    
    def insert_end(self, data):
        self.insert_at_nth(len(self), data)
    
    def insert_start(self, data):
        self.insert_at_nth(0, data)
        
    def insert_at_nth(self, index: int, data):
        """
        >>> linked_list = DoublyLinkedList()
        >>> linked_list.insert_at_nth(-1, 666)
        Traceback (most recent call last):
        ....
        IndexError: list index out of range
        >>> linked_list.insert_at_nth(1, 666)
        Traceback (most recent call last):
        ......
        IndexError: list index out of range
        >>> linked_list.insert_at_nth(0, 2)
        >>> linked_list.insert_at_nth(0, 1)
        >>> linked_list.insert_at_nth(2, 4)
        >>> linked_list.insert_at_nth(2, 3)
        >>> str(linked_list)
        '1->2->3->4'
        >>> linked_list.insert_at_nth(5, 5)
        Traceback (most recent call last):
        ....
        IndexError: list index out of range
        """
        # Index check
        if not 0 <= index <= len(self):
            raise IndexError("list index out of range")
        
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        elif index == 0:
            self.head.previous_node = new_node
            new_node.next_node = self.head
            self.head = new_node
        elif index == len(self):
            self.tail.next_node = new_node
            new_node.previous_node = self.tail
            self.tail = new_node
        else:
            temp = self.head
            for i in range(0, index):
                temp = temp.next_node
            temp.previous_node.next_node = new_node
            new_node.previous_node = temp.previous_node
            new_node.next_node = temp
            temp.previous_node = new_node
        
    def delete_head(self):
        return self.delete_nth(0)
    
    def delete_tail(self):
        return self.delete_nth(len(self) - 1) 
    
    def delete_nth(self, index: int):
        """
        >>> linked_list = DoublyLinkedList()
        >>> linked_list.delete_nth(0)
        Traceback (most recent call last):
        ....
        IndexError: list index out of range
        >>> for i in range(0, 5):
        ...     linked_list.insert_at_nth(i, i + 1)
        >>> linked_list.delete_nth(0) == 1
        True
        >>> linked_list.delete_nth(3) == 5
        True
        >>> linked_list.delete_nth(1) == 3
        True
        >>> str(linked_list)
        '2->4'
        >>> linked_list.delete_nth(2)
        Traceback (most recent call last):
        ....
        IndexError: list index out of range
        """
        if not 0 <= index <= len(self) - 1:
            raise IndexError("list index out of range")
        delete_node = self.head # default first node
        if len(self) == 1:
            self.head = self.tail = None
        elif index == 0:
            self.head = self.head.next_node
            self.head.previous_node = None
        elif index == len(self) - 1:
            delete_node = self.tail
            self.tail = self.tail.previous_node
            self.tail.next_node = None
        else:
            temp = self.head
            for i in range(0, index):
                temp = temp.next_node
            delete_node = temp
            temp.next_node.previous_node = temp.previous_node
            temp.previous_node.next_node = temp.next_node
        return delete_node.data
    
    def delete(self, data) -> str:
        current = self.head
        
        # Find node to delete
        while current.data != data:
            if current.next_node:
                current = current.next_node
            else: # We have reached end w/o finding given data
                return "No data found matching given value."
        
        if current == self.head:
            self.delete_head()
        elif current == self.tail:
            self.delete_tail()
        else: # Before: a <--> b (current) <--> c
            current.previous_node.next_node = current.next_node # a --> c
            current.next_node.previous_node = current.previous_node # a <--> c
        return data
    
    def is_empty(self):
        """
        >>> linked_list = DoublyLinkedList()
        >>> linked_list.is_empty()    
        True
        >>> linked_list.insert_end(1)
        >>> linked_list.is_empty()
        False
        """
        return len(self) == 0


def test_doubly_linked_list() -> None:
    """
    >>> test_doubly_linked_list()
    """
    linked_list = DoublyLinkedList()
    assert linked_list.is_empty() is True
    assert str(linked_list) == ""
    
    try:
        linked_list.delete_head()
        assert False # This should not happen
    except IndexError:
        assert True # This should happen
    
    try:
        linked_list.delete_tail()
        assert False # This should no happen
    except IndexError:
        assert True # This should happen
        
    for i in range(10):
        assert len(linked_list) == i
        linked_list.insert_at_nth(i, i + 1)
    assert str(linked_list) == "->".join(str(i) for i in range(1, 11))
    
    linked_list.insert_start(0)
    linked_list.insert_end(11)
    assert str(linked_list) == "->".join(str(i) for i in range(0, 12))
    
    assert linked_list.delete_head() == 0
    assert linked_list.delete_nth(9) == 10
    assert linked_list.delete_tail() == 11
    assert len(linked_list) == 9
    assert str(linked_list) == "->".join(str(i) for i in range(1, 10))
    
    assert linked_list.delete(8) == 8


if __name__ == "__main__":
    from doctest import testmod
    
    testmod()