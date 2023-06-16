class Node :
    def __init__(self, value , nextNode=None):
        self.value = value
        self.nextNode = nextNode


class LinkedList:
    def __init__(self,head = None):
        self.head = head


    def insert(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        currentNode = self.head


        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode


    def prinlist(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value,'->',end = ' ')

            currentNode = currentNode.nextNode

        print('None')
    def insertFirst(self,value):
        node = Node(value)
        node.nextNode=self.head
        self.head = node

    def insertAfterNodes(self,prev,value):

        if not prev :
            print('no node found ')
            return
        newNode = Node(value)
        newNode.nextNode= prev.nextNode
        prev.nextNode = newNode




l1 =LinkedList()
l1.insert(5)
l1.insert(5)
l1.insert(5)
l1.insert(5)
l1.insertFirst(0)
l1.insert(7)
#l1.insertAfterNodes(l1.head.nextNode,10)
l1.prinlist()

# Find the node with value 7
currentNode = l1.head
while currentNode is not None:
    if currentNode.value == 7:
        break
    currentNode = currentNode.nextNode

# Add a new node with value 10 after the node with value 7
if currentNode is not None:
    l1.insertAfterNodes(currentNode, 10)

l1.prinlist()