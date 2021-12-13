import math

class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_head(self, value):
        # Create new node
        new_node = LinkedList.Node(value)
        # If the list is empty, point both head and tail to new node
        if self.head is None:
            self.tail = new_node
            self.head = new_node
        # If the list is not empty, then only self.head will be affected
        else:
            # Implement adding nodes at the front (You can refer to the module)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def sqrt_num(self, value):
        # Implement the given task. Use Test Cases
        if (10 <= value and value <= 100):
            return math.sqrt(value)

# Test Case 1: sqrt_num function returns square root
# Expected Output: 3
num = LinkedList()
print(num.sqrt_num(9))
# Defect(s) Found: No defects

# Test Case 2: Inserting from head
# Expected Output: 9
linkedList = LinkedList()
linkedList.insert_head(81)
linkedList.insert_head(9) # This should not be added since it is not within 10 <= x <= 100
print(linkedList)
# Defect(s) Found: Nothing
