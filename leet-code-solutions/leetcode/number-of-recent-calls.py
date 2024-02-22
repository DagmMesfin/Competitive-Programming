class RecentCounter(object):

    def __init__(self):
        self.start = None
        self.end = None
        self.length = 0

    def ping(self, t):
        newnode = ListNode(t)
        if not self.start:
            self.start = newnode
            self.end = newnode
        else:
            self.end.next = newnode
            self.end = newnode
        self.length+=1

        while self.start and self.length and self.start.val < t-3000:
            self.start = self.start.next
            self.length -= 1

        return self.length
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)