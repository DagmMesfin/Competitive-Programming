# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [-1]*k
        self.length = 0
        self.start = -1
        self.end = -1
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.start == -1:
            self.start += self.k
            self.end += self.k
            self.deque[self.start] = value
            self.length += 1
        elif self.length == self.k:
            return False
        else:
            self.start -= 1
            self.deque[self.start] = value
            self.length += 1
        if self.start == -1:
            self.start += self.k
        return True


    def insertLast(self, value: int) -> bool:
        if self.start == -1:
            self.start += 1
            self.end += 1
            self.deque[self.start] = value
            self.length += 1
        elif self.length == self.k:
            return False
        else:
            self.end += 1
            self.end %= self.k
            self.deque[self.end] = value
            self.length += 1
        return True

    def deleteFront(self) -> bool:
        if self.length == 0:
            return False
        else:
            self.deque[self.start] = -1
            self.start += 1
            self.length -= 1
        if self.start == self.k:
            self.start %= self.k
        if self.length == 0:
            self.start = -1
            self.end = -1
        return True

    def deleteLast(self) -> bool:
        if self.length == 0:
            return False
        else:
            self.deque[self.end] = -1
            self.end -= 1
            self.length -= 1
        if self.end == -1:
            self.end += self.k
        if self.length == 0:
            self.start = -1
            self.end = -1
        return True

    def getFront(self) -> int:
        return self.deque[self.start]

    def getRear(self) -> int:
        return self.deque[self.end]
        

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.k