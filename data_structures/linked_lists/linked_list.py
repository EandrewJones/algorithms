'''
Example of a linked list implementation
'''


class Node:
    
    def __init__(self, data):
        self.data = data
        self.next_node = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.num_of_nodes = 0
        
    
    def insert_start(self, data):
        '''
        Inserts new node at beginning of linked list
        
        run-time: O(1)
        
        parameters
        ----------
        data: {array-like}
            An arbitrary data structure to store in first node
        
        returns
        -------
        None    
        '''
        # Increase number of nodes
        self.num_of_nodes +=1
        
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node    
        
    def insert_end(self, data):
        '''
        Inserts new node at the end of the linked list
        
        runtime: O(N)
        
        parameters
        ----------
        data: {array-like}
            Arbitrary data object to store in node.
            
        returns
        -------
        None
        '''
        # Update number of nodes
        self.num_of_nodes += 1
        
        # Instantiate new node
        new_node = Node(data)
        
        # Find end of linked list
        actual_node = self.head
        while actual_node.next_node is not None:
            actual_node = actual_node.next_node
            
        # Append new node at end
        actual_node.next_node = new_node
        
    def remove_node(self, data):
        '''
        Traverse node searching for node with given data value and
        remove from linked list.
        
        Parameters
        ----------
        data: {array-like}
            Item to be search for and removed from data structure
        
        Returns
        -------
        None
        '''
        if self.head is None:
            return
        
        actual_node = self.head
        previous_node = None
        
        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node
            
        # Search miss
        if actual_node is None:
            return
        
        # Remove head node
        if previous_node is None:
            self.head = actual_node.next_node
        # Remove internal node
        else:
            previous_node.next_node = actual_node.next_node
            
        # Decrement number of nodes
        self.num_of_nodes -= 1
        
    def size_of_list(self):
        '''O(1) runtime'''
        return self.num_of_nodes
    
    def traverse(self):
        '''Iterate over list and print nodes.
        O(n) runtime
        '''
        actual_node = self.head
        
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next_node
            
    
if __name__ == "__main__":
    
    # Test
    linked_list = LinkedList()
    linked_list.insert_start('Adam')
    linked_list.insert_start('Eve')
    linked_list.insert_start(100)
    linked_list.insert_end([50, 'b', 'c', 143.34])
    
    linked_list.traverse()
    print("Size: {}\n".format(linked_list.size_of_list()))
    
    print('------------------')
    linked_list.remove_node('Eve')
    linked_list.traverse()
    print("Size: {}\n".format(linked_list.size_of_list()))
    
    