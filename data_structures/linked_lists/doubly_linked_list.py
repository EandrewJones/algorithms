'''
Example of a doubly-linked list implementation
'''

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous_node = None
        
        
class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_of_nodes = 0
        
    def insert_end(self, data):
        self.num_of_nodes += 1
        
        new_node = Node(data)
        
        # When linked list is empty first and last nodes equal
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # Otherwise we insert the new node at the end
        else:
            new_node.previous_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node
        
    def insert_start(self, data):
        self.num_of_nodes += 1
        
        new_node = Node(data)
        
        # When linked list is empty first and last nodes equal
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
        # Otherwise insert new node at the beginning
        self.head.previous_node = new_node
        new_node.next_node = self.head
        self.head = new_node

    # TODO: Fix problem with reference pointers when removing internal node.
    def remove_node(self, data):
        if self.head is None:
            return
        
        current_node = self.head
        previous_node = None
        next_node = None
        
        while current_node is not None and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next_node
            
        # Search miss
        if current_node is None:
            return
        
        # Remove head node
        if previous_node is None:
            current_node.next_node.previous_node = None
            self.head = current_node.next_node            
        # Remove tail node
        elif next_node is None:
            previous_node.next_node = None
            self.tail = previous_node
        # Remove internal node
        else:
            previous_node.next_node = current_node.next_node
            current_node.next_node.previous_node = previous_node
            
        # Decrement number of nodes
        self.num_of_nodes -= 1
        
    def traverse_forward(self):
        
        current_node = self.head
        
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node
            
    def traverse_backward(self):
        
        current_node = self.tail
        
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.previous_node

    
if __name__ == "__main__":
    list = DoublyLinkedList()
    list.insert_end(1)
    list.insert_end('new head node')
    list.insert_end(['this', 'is', 'a', 'list', 1, 2, 3])
    
    print('------------Traverse forward--------------')
    list.traverse_forward()
    
    print('------------Traverse backward--------------')
    list.traverse_backward()
    
    print('Remove node == 2 and traverse forward')
    list.remove_node(2)
    list.traverse_forward()
    
    print('Remove node == "new head node" and traverse forward')
    list.remove_node('new head node')
    list.traverse_forward()