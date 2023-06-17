class Node:
    def __init__(self, value , nextNode = None):
        self.value = value
        self.nexNode = nextNode


class LinkedList :
    def __init__(self, head = None):
        self.head = head


    def insert(self,value):
        node = Node(value)
        if self.head is None:
            node = self.head
            self.head = node