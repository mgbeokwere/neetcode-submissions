class ListNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr != self.tail:
            if i == index:
                return curr.value
            curr = curr.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        head = self.head
        new_node.prev = head
        new_node.next = head.next

        head.next.prev = new_node
        head.next = new_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        tail = self.tail
        new_node.next = tail
        new_node.prev = tail.prev

        tail.prev.next = new_node
        tail.prev = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next
        i = 0
        new_node = ListNode(val)

        while True:
            if i == index:
                new_node.next = curr
                new_node.prev = curr.prev
                curr.prev.next = new_node
                curr.prev = new_node
                return

            if curr == self.tail:
                return

            curr = curr.next
            i += 1

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        i = 0

        while True:
            if curr == self.tail:
                return

            if i == index:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                return

            curr = curr.next
            i += 1