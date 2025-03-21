#Stack Class Implementation
class Stack:
    #creates a stack with capacity of 10
    def __init__(self, cap=10):
        self.capacity_value = cap
        #create a list with None value with capacity of 10
        self.stack = [None] * self.capacity_value
        #stack is empty
        self.size = 0
#Returns the capacity (how much it can hold)
    def capacity(self):
        return self.capacity_value
#add to top of stack
    def push(self, data):
        #if the current size is equal to capacity
        if self.size == self.capacity_value:
            #make more room
            self.resize()
        #add the new element to next available space
        self.stack[self.size] = data
        #The new element is added
        self.size += 1
#remove from top
    def pop(self):
        #If it's empty, display index error below:
        if self.is_empty():
            raise IndexError('pop() used on empty stack')
        #decrease one to reflect that we removed one element
        self.size -= 1
        #The stack still holds the value, but we pretend it's not there
        #because count size is decreased
        return self.stack[self.size]
#returns the element from top
    def get_top(self):
        #if it's empty, then no access
        if self.is_empty():
            return None
        #if it's not empty, return the topmost element
        #here: self.size - 1 we have -1 for index 
        return self.stack[self.size - 1]
#check if stack is empty
    def is_empty(self):
        return self.size == 0
#current number of elements 
    def __len__(self):
        return self.size

    def resize(self):
        #create a new capacity: double capacity
        new_capacity = self.capacity_value * 2
        #create a new stack with None values with the new capacity
        new_stack = [None] * new_capacity
        #copy all existing elements to the new stack
        for i in range(self.size):
            new_stack[i] = self.stack[i]
        #REPLACE old stack with new stack
        self.stack = new_stack
        #update capacity
        self.capacity_value = new_capacity
#Queue Class Implementation:FIFO(first in, first out)
#adding to rear(back)
#removing from front
class Queue:
    def __init__(self, cap=10):
        self.capacity_value = cap
        #list of None values with capacity of 10
        self.queue = [None] * self.capacity_value
        #track front
        self.front = 0
        #number of elements
        self.size = 0
#Returns the capacity (how much it can hold)
    def capacity(self):
        return self.capacity_value
#add to back(rear)
    def enqueue(self, data):
        #If it's full resize it
        if self.size == self.capacity_value:
            self.resize()
        #Circular behavior:
        #we add element to rear(or back)
        #self.front + self.size : position after the last element
        #% self.capacity_value: when reaching end of the list, go to beginning
        #(front + size) % capacity
        #when rear becomes 0, we go to the start of the list, because it reached the end
        rear = (self.front + self.size) % self.capacity_value
        #add data to our new rear
        self.queue[rear] = data
        #add one to reflect the element added
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('dequeue() used on empty queue')
        #data will store the front element
        data = self.queue[self.front]
        self.queue[self.front] = None  # Optional step not in requirement: Clear the slot
        #why did I include it?
        #because when we remove an element, it's still in the list we just ignore it
        #But with self.queue[self.front] = None, we replace that element with None
        #it's more clean
        #front moves forward by 1, when it reaches back, it comes back to index 0
        self.front = (self.front + 1) % self.capacity_value
        self.size -= 1
        return data
#return the element from front without removing it 
    def get_front(self):
        if self.is_empty():
            return None
        #using queue (what is stored)
        return self.queue[self.front]
#check if stack is empty
    def is_empty(self):
        return self.size == 0
#current number of elements 
    def __len__(self):
        return self.size

    def resize(self):
        new_capacity = self.capacity_value * 2
        new_queue = [None] * new_capacity
        for i in range(self.size):
            #circular behavior:
            #i is the position of new queue(which starts from 0)
            #for example if we have a queue like this:
            # [15, None, None, 5, 10] if the first element added is  in index 3(value 5), size is 3
            #for i=0: new_queue[0] = self.queue[(3 + 0) % 5]  # = self.queue[3] = 5
            # so the new element: [5, (9 other elements)] and we do it over and over
            new_queue[i] = self.queue[(self.front + i) % self.capacity_value]
        self.queue = new_queue
        self.front = 0
        self.capacity_value = new_capacity
#Deque Class Implementation: Double ended Queue
#we can add and remove from both front and back
#FIFO + LIFO
class Deque:
    def __init__(self, cap=10):
        self.capacity_value = cap
        self.deque = [None] * self.capacity_value
        self.front = 0
        self.size = 0

    def capacity(self):
        return self.capacity_value
#add to front
    def push_front(self, data):
        if self.size == self.capacity_value:
            self.resize()
        #Circular behavior
        self.front = (self.front - 1) % self.capacity_value
        self.deque[self.front] = data
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError('pop_front() used on empty deque')
        data = self.deque[self.front]
        self.deque[self.front] = None  # Optional not in requirement: Clear the slot
        #Circular behavior, like dequeue
        self.front = (self.front + 1) % self.capacity_value
        self.size -= 1
        return data

    def push_back(self, data):
        if self.size == self.capacity_value:
            self.resize()
        #like the enqueue
        rear = (self.front + self.size) % self.capacity_value
        self.deque[rear] = data
        self.size += 1

    def pop_back(self):
        if self.is_empty():
            raise IndexError('pop_back() used on empty deque')
        rear = (self.front + self.size - 1) % self.capacity_value
        data = self.deque[rear]
        self.deque[rear] = None  # Optional not in requirement: Clear the slot
        self.size -= 1
        return data

    def get_front(self):
        if self.is_empty():
            return None
        return self.deque[self.front]

    def get_back(self):
        if self.is_empty():
            return None
        #finding the index of back element
        #fist element and lest element. If it's goes out of scope
        #Then % helps it to  go to the beginning
        rear = (self.front + self.size - 1) % self.capacity_value
        return self.deque[rear]

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size
#give random access to an element(from front)
    def __getitem__(self, k):
        #if the key index is out of bounds
        if k < 0 or k >= self.size:
            raise IndexError('Index out of range')
        return self.deque[(self.front + k) % self.capacity_value]

    def resize(self):
        new_capacity = self.capacity_value * 2
        new_deque = [None] * new_capacity
        for i in range(self.size):
            new_deque[i] = self.deque[(self.front + i) % self.capacity_value]
        self.deque = new_deque
        self.front = 0
        self.capacity_value = new_capacity
