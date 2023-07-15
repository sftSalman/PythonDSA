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

    def search(self,value):
        currentNode = self.head
        while currentNode is not None:
            if currentNode.value == value:
                return True
            currentNode = currentNode.nextNode
        return False
    def rev_it(self):
        prev = None
        cur = self.head
        while cur :
            nxt = cur.nextNode
            cur.nextNode = prev
            prev = cur
            cur = nxt
        self.head = prev
    def swap(self,k1,k2):
        if k1 == k2 :
            return
        prev1 = None
        cur1 = self.head
        while cur1 and cur1.value != k1:


            prev1 = cur1
            cur1=cur1.nextNode



        prev2 = None
        cur2 = self.head
        while cur2 and cur2.value != k2:


            prev2 = cur2
            cur2=cur2.nextNode


        if not cur1 or not cur2:
            return
        if prev1:
            prev1.nextNode = cur2
        else:
            self.head = cur2
        if prev2:
            prev2.nextNode = cur1
        else:
            self.head = cur1
        cur1.nextNode ,cur2.nextNode = cur2.nextNode,cur1.nextNode






    # def reverse(self):
    #     def rev_until(currentNode, prevNode):
    #         if currentNode is None:
    #             return prevNode
    #         self.head = reverse()


# Create a linked list object
l1 = LinkedList()

# Insert values at the beginning and print the list
l1.insert(6)
l1.printList()

l1.insert(7)
l1.printList()

l1.insert(8)
l1.printList()
print(l1.search(10))
l1.rev_it()
l1.printList()
l1.swap(7,6)
l1.printList()