class RandomizedSet:

    def __init__(self):
        self.randomset = {}        

    def insert(self, val: int) -> bool:
        if val in self.randomset:
            return False
        
        self.randomset[val] = 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.randomset:
            return False

        del self.randomset[val]
        return True

    def getRandom(self) -> int:
        return random.choice(list(self.randomset.keys()))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()