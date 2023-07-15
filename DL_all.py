class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data,'->',end = ' ')
            cur = cur.next
        print('None')
    def add_after_node(self,key,data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data==key:
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next =nxt
                new_node.prev = cur
                nxt.prev = new_node
            cur = cur.next


    def add_before_node(self,key,data):

        cur = self.head
        while cur:
            if cur.prev is None and cur.data ==key:
                self.prepend(data)
                return
            elif cur.data ==key:
                new_node = Node(data)
                prev = cur.prev
                prev.next= new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = prev
            cur= cur.next

    def  reverse(self):
        tmp = None
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur= cur.prev
        if tmp:
            self.head = tmp.prev

    def pairs_with_sum(self,sum_val):
        pairs = list()
        p = self.head
        q = None
        while p:
            q = p.next
            while q:
                if p.data + q.data == sum_val:
                    pairs.append(p.data, q.data)
                q = q.next
            p = p.next

        return pairs











dllist = DoublyLinkedList()
dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(5)
dllist.add_after_node(1,11)
dllist.add_before_node(1,12)

dllist.print_list()
dllist.reverse()
dllist.print_list()
print(dllist.pairs_with_sum(12))
