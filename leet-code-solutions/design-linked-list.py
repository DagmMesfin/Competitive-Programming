class Node:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        currentval = self.head
        i = 0
        while currentval:
            if i == index:
                return currentval.val
            i+=1
            currentval = currentval.next
            
        if not currentval:
            return -1

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length+=1

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = Node(val)
        if index == self.length:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            temp = self.head
            i = 0
            while temp:
                if i == index-1:
                    prev = temp
                    temp = newNode
                    temp.next = prev.next
                    prev.next = temp
                    break
                temp = temp.next
                i+=1
            self.length+=1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return None
        elif index == 0:
            temp = self.head.next
            self.head.next = None
            self.head = temp
            self.length-=1
        else:
            temp = self.head
            i = 0
            while temp:
                if i == index-1:
                    prev = temp
                    temp = temp.next
                    prev.next = temp.next
                    if not temp.next:
                        self.tail = prev
                    break
                temp = temp.next
                i+=1
            self.length-=1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)