class RandomizedSet(object):

    def __init__(self):
        self.randomset = {}
        self.arr = []
        self.length = 0
        
    def insert(self, val):
        if val in self.randomset:
            return False
        
        self.randomset[val] = self.length
        self.length += 1
        self.arr.append(val)
        return True
        

    def remove(self, val):
        if val not in self.randomset:
            return False

        indo = self.randomset[val]

        if indo == self.length - 1:
            del self.randomset[val]
            self.arr.pop()
            self.length -= 1
            return True

        self.arr[indo], self.arr[-1] = self.arr[-1], self.arr[indo]
        self.arr.pop()
        del self.randomset[val]
        self.randomset[self.arr[indo]] = indo
        self.length -= 1
        
        return True
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()