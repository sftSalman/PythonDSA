class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[-1]

    def size(self):
        return len(self.stack)



# Create a new stack
my_stack = Stack()

# Check if the stack is empty
print(my_stack.is_empty())  # Output: True

# Add elements to the stack
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

# Check the size of the stack
print(my_stack.size())  # Output: 3

# Peek at the top element
print(my_stack.peek())  # Output: 30

# Remove elements from the stack
print(my_stack.pop())  # Output: 30
print(my_stack.pop())  # Output: 20

# Check the size of the stack again
print(my_stack.size())  # Output: 1
