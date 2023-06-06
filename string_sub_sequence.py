class linkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = linkedListNode(value)
        if self.head is None:
            self.head = node
            return
        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode

def printList(list):
    currentNode = list.head
    while currentNode is not None:
        print(currentNode.value, '->', end=' ')
        currentNode = currentNode.nextNode
    print('None')

# Create a linked list object
l1 = LinkedList()

# Insert a value and print the list
l1.insert(6)
printList(l1)

# Insert another value and print the list
l1.insert(7)
printList(l1)
