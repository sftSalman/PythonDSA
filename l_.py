class Node:
    def __init__(self,value,nextNode=None):
        self.value = value
        self.nextNode = nextNode



class Linkedlist:
    def __init__(self,head=None):
        self.head = head


    def insert(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        current_node = self.head
        while True:
            if current_node.nextNode is None:
                current_node.nextNode = node
                break
            current_node = current_node.nextNode


    def printl(self):
        current_node = self.head
        while current_node.nextNode is not None:
            print(current_node.value , '->', end = ' ')
            current_node = current_node.nextNode

        print('None')


    def lenght(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count = count +1
            current_node = current_node.nextNode
        return count




n1 = Linkedlist()
n1.insert(5)
n1.insert(6)
n1.insert(7)
n1.insert(8)
n1.insert(9)
n1.printl()

