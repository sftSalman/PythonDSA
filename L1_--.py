class Node:
    def __init__(self, value , nextNode = None):
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

        while True :
            if currentNode.nextNode is None :
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode

    def printList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value,'->', end = ' ')
            currentNode = currentNode.nextNode


        print('None')

    def search(self,value):
        currentNode = self.head
        while currentNode is not None:
            if currentNode.value == value:
                return True
            currentNode = currentNode.nextNode
        return False

    def reverse(self):
        def reverse_until (currentNode, prevNode):
            if currentNode is None:
                return prevNode
            nextNode = currentNode.nextNode
            currentNode.nextNode = prevNode
            return reverse_until(nextNode,currentNode)

        self.head = reverse_until(currentNode = self.head , prevNode = None)





l1 = LinkedList()
l1.insert(5)
l1.printList()
l1.insert(6)
l1.printList()
#print(l1.search(5))
l1.insert(8)
l1.printList()
l1.insert(9)
l1.printList()