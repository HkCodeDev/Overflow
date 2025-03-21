#Node implementation
class Node:
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.prev
#SortedList Class Implementation
class SortedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_front(self):
        return self.head

    def get_back(self):
        return self.tail

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def insert(self, data):
        new_node = Node(data)
        if self.is_empty():
            # List is empty, set new node as head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # Find the proper position to insert the new node
            current = self.head
            while current is not None and current.get_data() < data:
                current = current.get_next()

            if current is None:
                # Insert at the end
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            elif current == self.head:
                # Insert at the beginning
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            else:
                # Insert in the middle
                previous_node = current.get_previous()
                new_node.next = current
                new_node.prev = previous_node
                previous_node.next = new_node
                current.prev = new_node

        self.size += 1
        return new_node

    def erase(self, node):
        if node is None:
            raise ValueError('Cannot erase node referred to by None')

        if node == self.head:
            # Erasing the head node
            self.head = node.get_next()
            if self.head is not None:
                self.head.prev = None
        elif node == self.tail:
            # Erasing the tail node
            self.tail = node.get_previous()
            if self.tail is not None:
                self.tail.next = None
        else:
            # Erasing a node in the middle
            prev_node = node.get_previous()
            next_node = node.get_next()
            prev_node.next = next_node
            next_node.prev = prev_node

        self.size -= 1

    def search(self, data):
        current = self.head
        while current is not None:
            if current.get_data() == data:
                return current
            current = current.get_next()
        return None

