

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # ... (rest of the code)

    def find_node_by_data(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def swap(self, data1, data2):
        node1 = self.find_node_by_data(data1)
        node2 = self.find_node_by_data(data2)

        if node1 is None or node2 is None:
            print("One or both of the nodes not found in the list.")
            return

        if node1 == node2:
            return

        prev_node1 = node1.prev
        next_node1 = node1.next
        prev_node2 = node2.prev
        next_node2 = node2.next

        if prev_node1:
            prev_node1.next = node2
        else:
            self.head = node2

        if next_node1:
            next_node1.prev = node2

        node2.prev = prev_node1
        node2.next = next_node1
        node1.prev = prev_node2
        node1.next = next_node2

        if prev_node2:
            prev_node2.next = node1

        if next_node2:
            next_node2.prev = node1

    # ... (rest of the code)
dllist = DoublyLinkedList()
dllist.append(3)
dllist.append(2)
dllist.append(8)
dllist.append(4)
dllist.append(2)

dllist.print_list()  # Output: 3 2 8 4 2
dllist.swap(3, 4)
dllist.print_list()  # Output: 4 2 8 3 2
