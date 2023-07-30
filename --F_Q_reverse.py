class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[0]

    def size(self):
        return len(self.queue)
def reverse_string(Queue, input_str):

    # Loop through the string and push contents
    # character by character onto stack.
    for i in range(len(input_str)):
        Queue.enqueue(input_str[i])

    rev_str = ""
    while not Queue.is_empty():
        rev_str = Queue.dequeue()+ rev_str

    return rev_str
# Create a new queue
my_queue = Queue()

# Check if the queue is empty
print(my_queue.is_empty())  # Output: True

# Add elements to the queue
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
queue = Queue()
input_str = "1234567"
print(reverse_string(queue, input_str))

# Check the size of the queue
# print(my_queue.size())  # Output: 3
#
# # Peek at the front element
# print(my_queue.peek())  # Output: 10
#
# # Remove elements from the queue
# print(my_queue.dequeue())  # Output: 10
# print(my_queue.dequeue())  # Output: 20
#
# # Check the size of the queue again
# print(my_queue.size())  # Output: 1