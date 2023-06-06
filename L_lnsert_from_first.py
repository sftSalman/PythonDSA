class linkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = linkedListNode(value)
        node.nextNode = self.head
        self.head = node

    def printList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, '->', end=' ')
            currentNode = currentNode.nextNode
        print('None')

# Create a linked list object
l1 = LinkedList()

# Insert values at the beginning and print the list
l1.insert(6)
l1.printList()

l1.insert(7)
l1.printList()

l1.insert(8)
l1.printList()
