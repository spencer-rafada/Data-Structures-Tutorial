class LinkedList:
    """
    Implementation of the Linked List data structure. The node class below is an inner class.
    It is related to the outer class Linked list.
    """
    class Node:
        """
        Each node of the linked list will have data pointing to the previous and next node
        """

        def __init__(self, data):
            """
            Initializing a node. The links are unknown since we do not know where we will put it yet.
            """
            self.data = data
            self.prev = None
            self.next = None
    
    def __init__(self):
        """
        Initializing an empty linkedlist
        """
        self.head = None
        self.tail = None
    
    def insert_fastest(self, value):
        """
        Inserting the fastest at the head of the linked list.
        """
        # Create the new node
        new_node = LinkedList.Node(value)

        # If the list is empty, point both head and tail to new node
        if self.head is None:
            pass
        # If the list is not empty, then only self.head will be affected
        else:
            # Implement adding nodes at the front (You can refer to the module)
            pass

    def insert_middle(self, value):
        """
        Insert value in the Linked List
        """
        # Search for the first occurence where value is less than curr.next.data
        curr = self.head
        new_node = LinkedList.Node(value)
        while curr is not None:
            if curr.data == value:
                # If the first occurance is at the tail, we will add from the tail
                if curr == self.tail:
                    pass
                    # Implement adding from the tail/back.
                else:
                    # Implement adding from the middle of the linked list.
                    # Be mindful of your links.
                    pass
                return # We exit the function once the value is found.
            curr = curr.next

    def remove_time(self, value):
        """
        Remove the first node with the data that is equal to value
        """
        # Search for the node that matches 'value' by starting from head
        curr = self.head
        while curr is not None:
            if value == curr.data:
                if curr == self.head:
                    # Implement removing from head
                    pass
                elif curr == self.tail:
                    # Implement removing from tail
                    pass
                else:
                    # Implement removing from middle
                    pass
                return # We exit the function once it is removed
            curr = curr.next

    def insert_slowest(self, value):
        """
        Inserting the slowest lap time at the tail
        """
        # Create a new node
        new_node = LinkedList.Node(value)

        # If the linked list is empty, we set the head and tail to the new node
        if self.head == None:
            pass
        # If the linked list is not empty, we set the new value to tail
        else:
            # Implement adding from tail
            pass
    
    def insert_lap_times(self, value):
        """
        Inserting lap time
        """
        # Search if value is in list from head
        # Call the write function in each conditional statements
        if value < self.head.data:
            pass
        elif value > self.tail.data:
            pass
        else:
            pass


# Create Empty Linked List
lap_times = LinkedList()
print("Empty Lap Times: {}\n".format(lap_times))

# ======= TASK 1 ======= #
# Test Case 1: Inserting fastest lap times at lap times
# Expected Output: 
lap_times.insert_fastest(90)
lap_times.insert_fastest(80)
lap_times.insert_fastest(79.5)
print("Inserting 6 numbers: {}\n".format(lap_times))
# Defect(s) Found:

# ====== TASK 2 ====== #
# Test Case 2: Inserting slowest lap times at lap times
# Expected Output: 
lap_times.insert_slowest(100)
lap_times.insert_slowest(95)
print("Inserted 2 slowest times: {}\n".format(lap_times))

# ====== TASK 3 ====== #
# Test Case 3: Removing lap time due to penalty
# Expected Output:
lap_times.remove_time(95)
lap_times.remove_time(82) # not in list, so list won't be affected
print("Removed times with penalties: {}\n".format(lap_times))
# Defect(s) Found:

# ====== TASK 4 ====== #
# Test Case 4: Inserting in the middle
# Expected Output:
lap_times.insert_middle(85)
lap_times.insert_middle(88)
print("Inserted 2 middle times: {}\n".format(lap_times))
# Defect(s) Found:

# ====== STRETCH ====== #
# Test Case 5: 
# Expected Output:
lap_times_ordered = LinkedList()
lap_times_ordered.insert_lap_times(55)
lap_times_ordered.insert_lap_times(40)
lap_times_ordered.insert_lap_times(60)
lap_times_ordered.insert_lap_times(58)
print("Lap Times: {}\n".format(lap_times_ordered))
# Defect(s) Found: