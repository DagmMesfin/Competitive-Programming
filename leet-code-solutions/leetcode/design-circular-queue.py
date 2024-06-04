class MyCircularQueue:
    def __init__(self, k: int):
        self.head = ListNode(-1)
        self.tail = self.head
        self.cap = k
        self.len = 0
        for i in range(k-1):
            newnode = ListNode(-1)
            self.tail.next = newnode
            self.tail = self.tail.next
        self.tail.next = self.head
        self.tail = self.head


    def enQueue(self, value: int) -> bool:
        if self.tail.next.val != -1:
            return False
        if self.tail.val == -1:
            self.tail.val = value
        else:
            self.tail = self.tail.next
            self.tail.val = value
        return True
        


    def deQueue(self) -> bool:
        if self.head.val == -1:
            return False
        if self.head.next.val == -1:
            self.head.val = -1
        else:
            self.head.val = -1
            self.head = self.head.next
        return True

    def Front(self) -> int:
        return self.head.val

    def Rear(self) -> int:
        return self.tail.val

        

    def isEmpty(self) -> bool:
        return self.tail.val == -1
        

    def isFull(self) -> bool:
        return self.tail.next.val != -1
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()