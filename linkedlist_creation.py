class LinklistNode:
    def __init__(self,value,nextNode=None):
        self.value = value
        self.nextNode = nextNode


class linkedlist :
    def __init__(self, head=None) :
        self.head = head

    def insert(self, value) :
        node = LinklistNode ( value )
        if self.head is None :
            self.head = node
            return

        current_node = self.head

        while True :
            if current_node.nextNode is None :
                current_node.nextNode = node
                break
            current_node = current_node.nextNode

    def printLinkedList(self) :
        current_node = self.head
        while current_node is not None :
            # print(current_node.value,'->', end=" ")
            print ( current_node.value, '->', end = ' ' )
            current_node = current_node.nextNode

        print ( 'none' )
l1 = linkedlist()
l1.printLinkedList()
l1.insert('3')
l1.printLinkedList()
l1.insert('4')
l1.printLinkedList()
l1.insert('5')
l1.printLinkedList()