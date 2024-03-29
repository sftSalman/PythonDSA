# Youtube Video: https://www.youtube.com/watch?v=VD73579E3-o
#hhwht
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList :
    def __init__(self) :
        self.head = None

    def append(self, data) :
        if self.head is None :
            new_node = Node ( data )
            new_node.prev = None
            self.head = new_node
        else :
            new_node = Node ( data )
            cur = self.head
            while cur.next :
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self, data) :
        if self.head is None :
            new_node = Node ( data )
            new_node.prev = None
            self.head = new_node
        else :
            new_node = Node ( data )
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def print_list(self) :
        cur = self.head
        while cur :
            print ( cur.data )
            cur = cur.next

    def add_after_node(self, key, data) :
        cur = self.head
        while cur :
            if cur.next is None and cur.data == key :
                self.append ( data )
                return
            elif cur.data == key :
                new_node = Node ( data )
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                new_node.prev = cur
                nxt.prev = new_node
            cur = cur.next

    def add_before_node(self, key, data) :
        cur = self.head
        while cur :
            if cur.prev is None and cur.data == key :
                self.prepend ( data )
                return
            elif cur.data == key :
                new_node = Node ( data )
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = prev
            cur = cur.next

    def delete(self, key) :
        cur = self.head
        while cur :
            if cur.data == key and cur == self.head :
                # Case 1:
                if not cur.next :
                    cur = None
                    self.head = None
                    return

                # Case 2:
                else :
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return

            elif cur.data == key :
                # Case 3:
                if cur.next :
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return

                # Case 4:
                else :
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

    def delete_node(self, node) :
        cur = self.head
        while cur :
            if cur == node and cur == self.head :
                # Case 1:
                if not cur.next :
                    cur = None
                    self.head = None
                    return

                # Case 2:
                else :
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return

            elif cur == node :
                # Case 3:
                if cur.next :
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return

                # Case 4:
                else :
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

    def reverse(self) :
        tmp = None
        cur = self.head
        while cur :
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        if tmp :
            self.head = tmp.prev

    def remove_duplicates(self) :
        cur = self.head
        seen = dict ()
        while cur :
            if cur.data not in seen :
                seen[cur.data] = 1
                cur = cur.next
            else :
                nxt = cur.next
                self.delete_node ( cur )
                cur = nxt

    def bubble_sort(self) :
        if self.head is None or self.head.next is None :
            return

        n = self.length ()
        for i in range ( n ) :
            cur = self.head
            for j in range ( n - i - 1 ) :
                if cur.data > cur.next.data :
                    self.swap ( cur, cur.next )
                else :
                    cur = cur.next

    def swap(self, node1, node2) :
        if node1 == node2 :
            return

        prev_node1 = node1.prev
        next_node1 = node1.next
        prev_node2 = node2.prev
        next_node2 = node2.next

        if prev_node1 :
            prev_node1.next = node2
        else :
            self.head = node2

        if next_node1 :
            next_node1.prev = node2

        node2.prev = prev_node1
        node2.next = node1
        node1.prev = node2
        node1.next = next_node2

        if next_node2 :
            next_node2.prev = node1

    def length(self) :
        count = 0
        cur = self.head
        while cur :
            count += 1
            cur = cur.next
        return count




    def pairs_with_sum(self, sum_val) :
        pairs = list ()
        p = self.head
        q = None
        while p :
            q = p.next
            while q :
                if p.data + q.data == sum_val :
                    pairs.append ( "(" + str ( p.data ) + "," + str ( q.data ) + ")" )
                q = q.next
            p = p.next
        return pairs


dllist = DoublyLinkedList ()
dllist.append ( 3 )
dllist.append ( 2 )
dllist.append ( 8 )
dllist.append ( 4 )
dllist.append ( 2 )

#print(dllist.pairs_with_sum ( 10 ))
#dllist.print_list ()
#print('/')
#dllist.bubble_sort()
#dllist.print_list()
dllist.print_list()
dllist.swap(3,4)
dllist.print_list()