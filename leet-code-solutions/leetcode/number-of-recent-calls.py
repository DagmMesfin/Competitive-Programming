class RecentCounter(object):

    def __init__(self):
        self.pingo = []

    def ping(self, t):
        self.pingo.append(t)
        while self.pingo[0] < (t-3000):
            self.pingo.pop(0)
        return len(self.pingo)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)