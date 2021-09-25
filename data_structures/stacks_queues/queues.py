"""
Example of a queue implentation

Notes
-----

Queues are abstract data types and have a FIFO - first in, first out - structure

I will use our previous linked list data structure to implement the queue.
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __str__(self):
        return f"{self.data}"

class LinkedList:

    def __init__(self):
        self.head = None

    def __iter__(self):
        """
        >>> linked_list = LinkedList()
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
        >>> linked_list = LinkedList()
        >>> linked_list.insert_end('a')
        >>> linked_list.insert_end('b')
        >>> linked_list.insert_end('c')
        >>> str(linked_list)
        'a->b->c'
        """
        return "->".join([str(item) for item in self])

    def __len__(self):
        """
        >>> linked_list = LinkedList()
        >>> for i in range(0, 5):
        ...     linked_list.insert_at_nth(i, i+1)
        >>> len(linked_list) == 5
        True
        """
        return len(tuple(iter(self)))

    def insert_start(self, data):
        self.insert_at_nth(0, data)

    def insert_end(self, data):
        self.insert_at_nth(len(self), data)

    def insert_at_nth(self, index: int, data):
        """
        >>> linked_list = LinkedList()
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
            self.head = new_node
        elif index == 0:
            new_node.next_node = self.head
            self.head = new_node
        else:
            temp = self.head
            for i in range(0, index - 1):
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def delete_head(self):
        return self.delete_nth(0)

    def delete_tail(self):
        return self.delete_nth(len(self) - 1)

    def delete_nth(self, index: int):
        """
        >>> linked_list = LinkedList()
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
            raise IndexError('list index out of range')
        delete_node = self.head
        if len(self) == 1:
            self.head = None
        elif index == 0:
            self.head = self.head.next_node
        else:
            temp = self.head
            for i in range(0, index - 1):
                temp = temp.next_node
            delete_node = temp.next_node
            temp.next_node = temp.next_node.next_node
        return delete_node.data

    def delete(self, data) -> str:
        current = self.head

        # Find node to delete
        i = 0
        while current.data != data:
            if current.next_node:
                current = current.next_node
                i += 1
            else: # We have reached end w/o finding data
                return "No data found matching given value"

        if current == self.head:
            self.delete_head()
        else: # Before: a --> b (current) --> c
            self.delete_nth(i) # a --> c
        return data

    def is_empty(self):
        """
        >>> linked_list = LinkedList()
        >>> linked_list.is_empty()
        True
        >>> linked_list.insert_end(1)
        >>> linked_list.is_empty()
        False
        """
        return len(self) == 0

class Queue:

    def __init__(self):
        self.queue = LinkedList()

    def __str__(self):
        """
        >>> queue = Queue()
        >>> queue.enqueue('a')
        >>> queue.enqueue('b')
        >>> queue.enqueue('c')
        >>> str(queue)
        'a->b->c'
        """
        return str(self.queue)

    def __iter__(self):
        """
        >>> queue = Queue()
        >>> queue.enqueue('a')
        >>> queue.enqueue('b')
        >>> queue.enqueue('c')
        >>> tuple(queue)
        ('a', 'b', 'c')
        """
        return iter(self.queue)

    def __len__(self):
        """
        >>> queue = Queue()
        >>> for i in range(0, 5):
        ...     queue.enqueue(i)
        >>> len(queue) == 5
        True
        """
        return len(self.queue)

    # O(1) running time
    def is_empty(self):
        """
        >>> queue = Queue()
        >>> queue.is_empty()
        True
        >>> queue.enqueue(1)
        >>> queue.is_empty()
        False
        """
        return self.queue.is_empty()

    # O(N) running time
    # TODO: switch to doubly-linked list for O(N) running time
    def enqueue(self, data):
        """
        >>> queue = Queue()
        >>> for i in range(0, 5):
        ...     queue.enqueue(i+1)
        >>> str(queue)
        '1->2->3->4->5'
        """
        self.queue.insert_end(data=data)

    # O(1) running time
    def dequeue(self):
        """
        >>> queue = Queue()
        >>> for i in range(0, 5):
        ...     queue.enqueue(i+1)
        >>> queue.dequeue()
        1
        """
        if self.is_empty():
            raise IndexError('list index out of range')
        data = self.queue.head.data
        self.queue.delete_head()
        return data

    def peek(self):
        """
        >>> queue = Queue()
        >>> for i in range(0, 5):
        ...     queue.enqueue(i+1)
        >>> queue.peek()
        1
        """
        if self.is_empty():
            raise IndexError('list index out of range')
        return self.queue.head.data


def test_queue():
    """
    >>> test_queue()
    """
    queue = Queue()
    assert queue.is_empty() is True
    assert str(queue) == ""

    try:
        queue.dequeue()
        assert False # This should not happen
    except IndexError:
        assert True # This should happen

    try:
        queue.peek()
        assert False # This should not happen
    except IndexError:
        assert True # This should happen

    for i in range(10):
        assert len(queue) == i
        queue.enqueue(i)
    assert str(queue) == '->'.join([str(i) for i in range(10)])

    assert queue.dequeue() == 0
    assert queue.peek() == 1
    assert queue.dequeue() == 1
    assert queue.peek() == 2


if __name__ == "__main__":
    from doctest import testmod

    testmod()