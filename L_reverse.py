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

    def search(self, value):
        currentNode = self.head
        while currentNode is not None:
            if currentNode.value == value:
                return True
            currentNode = currentNode.nextNode
        return False

    def get_length(self):
        count = 0
        currentNode = self.head
        while currentNode is not None:
            count += 1
            currentNode = currentNode.nextNode
        return count

    def reverse(self):
        prevNode = None
        currentNode = self.head
        while currentNode is not None:
            nextNode = currentNode.nextNode
            currentNode.nextNode = prevNode
            prevNode = currentNode
            currentNode = nextNode
        self.head = prevNode

# Create a linked list object
l1 = LinkedList()

# Insert values at the beginning
l1.insert(6)
l1.insert(7)
l1.insert(8)

# Print the original list
print("Original list:")
l1.printList()

# Reverse the list
l1.reverse()

# Print the reversed list
print("Reversed list:")
l1.printList()
