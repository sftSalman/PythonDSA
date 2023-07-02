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


l1 = LinkedList()
l1.insert(5)
l1.printList()