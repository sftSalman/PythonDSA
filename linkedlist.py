class LinkedListNode:
    def __init__(self, value, next_Node=None):
        self.value = value
        self.next = next_Node

node1 = LinkedListNode('7')
node2 = LinkedListNode('2')
node3 = LinkedListNode('3')

node1.next = node2
node2.next = node3

currentNode = node1
while True:
    print(currentNode.value, '->')
    if currentNode.next is None:
        print('None')
        break
    currentNode = currentNode.next
