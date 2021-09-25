"""
Queue from stacks

Implement a queue only using stacks.

The implementation requires two stacks, one for the queue
and a swap stack using for reordering the queue during enqueues
or dequeues. The implementation requires that either the
enqueue or dequeue has O(n) running time.

You could use Python's built-in list data structure for stacks.
However, I use a custom wrapper around the list with some
additional functionality.
"""


class BaseQueue:
    """Base queue from stacks."""

    def __init__(self):
        self.queue = []
        self.swap = []

    def __str__(self):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        return len(self.queue)

    def is_empty(self):
        return self.queue == []

    def peek(self):
        pass


class QueueA(BaseQueue):
    """enQueue heavy running time."""

    def __str__(self):
        """
        >>> queue = QueueA()
        >>> queue.enqueue('a')
        >>> queue.enqueue('b')
        >>> queue.enqueue('c')
        >>> str(queue)
        'a > b > c'
        """
        return " > ".join(reversed([str(item) for item in self.queue]))

    def __iter__(self):
        """
        >>> queue = QueueA()
        >>> queue.enqueue('a')
        >>> queue.enqueue('b')
        >>> queue.enqueue('c')
        >>> tuple(queue)
        ('a', 'b', 'c')
        """
        for item in reversed(self.queue):
            yield item

    def __len__(self):
        """
        >>> queue = QueueA()
        >>> queue.enqueue('a')
        >>> queue.enqueue('b')
        >>> queue.enqueue('c')
        >>> len(queue)
        3
        """
        return super().__len__()

    def is_empty(self):
        """
        >>> queue = QueueA()
        >>> queue.is_empty()
        True
        >>> queue.enqueue('a')
        >>> queue.is_empty()
        False
        """
        return super().is_empty()

    def enqueue(self, data):
        """
        >>> queue = QueueA()
        >>> for i in range(0, 5):
        ...     queue.enqueue(i+1)
        >>> str(queue)
        '1 > 2 > 3 > 4 > 5'
        """
        # Move all elements from queue to swap
        while not self.is_empty():
            self.swap.append(self.queue[-1])
            self.queue.pop()

        # Push data to queue
        self.queue.append(data)

        # Move all items back to queue from swap
        while self.swap != []:
            self.queue.append(self.swap[-1])
            self.swap.pop()

    def dequeue(self):
        """
        >>> queue = QueueA()
        >>> for i in range(0, 5):
        ...     queue.enqueue(i+1)
        >>> queue.dequeue()
        1
        """
        if self.is_empty():
            raise IndexError("list index out of range")
        data = self.queue[-1]
        self.queue.pop()
        return data

    def peek(self):
        """
        >>> queue = QueueA()
        >>> for i in range(0, 5):
        ...     queue.enqueue(i+1)
        >>> queue.dequeue()
        1
        """
        if self.is_empty():
            raise IndexError("list index out of range")
        return self.queue[-1]


class QueueB(BaseQueue):
    """deQueue heavy running time."""

    def __str__(self):
        """
        >>> queue = QueueB()
        >>> queue.enqueue('a')
        >>> queue.enqueue('b')
        >>> queue.enqueue('c')
        >>> str(queue)
        'a > b > c'
        """
        return " > ".join([str(item) for item in self.queue])

    def __iter__(self):
        """
        >>> queue = QueueB()
        >>> queue.enqueue('a')
        >>> queue.enqueue('b')
        >>> queue.enqueue('c')
        >>> tuple(queue)
        ('a', 'b', 'c')
        """
        for item in self.queue:
            yield item

    def __len__(self):
        """
        >>> queue = QueueB()
        >>> queue.enqueue('a')
        >>> queue.enqueue('b')
        >>> queue.enqueue('c')
        >>> len(queue)
        3
        """
        return super().__len__()

    def is_empty(self):
        """
        >>> queue = QueueB()
        >>> queue.is_empty()
        True
        >>> queue.enqueue('a')
        >>> queue.is_empty()
        False
        """
        return super().is_empty()

    def enqueue(self, data):
        """
        >>> queue = QueueB()
        >>> for i in range(0, 5):
        ...     queue.enqueue(i+1)
        >>> str(queue)
        '1 > 2 > 3 > 4 > 5'
        """
        self.queue.append(data)

    def dequeue(self):
        """
        >>> queue = QueueA()
        >>> for i in range(0, 5):
        ...     queue.enqueue(i+1)
        >>> queue.dequeue()
        1
        """
        # Move all items from queue to swap
        while not self.is_empty():
            self.swap.append(self.queue[-1])
            self.queue.pop()

        # Grab first item
        data = self.swap[-1]
        self.swap.pop()

        # Return items to queue from swap
        while self.swap != []:
            self.queue.append(self.swap[-1])
            self.swap.pop()

        return data

    def peek(self):
        """
        >>> queue = QueueB()
        >>> for i in range(0, 5):
        ...     queue.enqueue(i+1)
        >>> queue.dequeue()
        1
        """
        if self.is_empty():
            raise IndexError('list index out of range')
        return self.queue[0]


def test_queue():
    """
    >>> test_queue()
    """
    queue_a, queue_b = (QueueA(), QueueB())
    queues = [queue_a, queue_b]
    for queue in queues:
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
        assert str(queue) == ' > '.join([str(i) for i in range(10)])

        assert queue.dequeue() == 0
        assert queue.peek() == 1
        assert queue.dequeue() == 1
        assert queue.peek() == 2


if __name__ == "__main__":
    from doctest import testmod

    testmod()