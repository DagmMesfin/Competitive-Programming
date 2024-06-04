class Bitset:

    def __init__(self, size: int):
        self.bitset = ['0']*size
        self.counto = 0
        self.countrev = size
        self.bitsetrev = ['1']*size
        self.n = size

    def fix(self, idx: int) -> None:
        if self.bitset[idx] != '1':
            self.bitset[idx] = '1'
            self.counto+=1
            self.bitsetrev[idx] = '0'
            self.countrev-=1

        

    def unfix(self, idx: int) -> None:
        if self.bitset[idx] != '0':
            self.bitset[idx] = '0'
            self.counto-=1
            self.bitsetrev[idx] = '1'
            self.countrev+=1

    def flip(self) -> None:
        temp = self.bitset
        tempcount = self.counto
        self.bitset = self.bitsetrev
        self.counto = self.countrev
        self.bitsetrev = temp
        self.countrev = tempcount

    def all(self) -> bool:
        return self.counto == self.n

    def one(self) -> bool:
        return self.counto > 0 


    def count(self) -> int:
        return self.counto

    def toString(self) -> str:
        return ''.join(self.bitset) 
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()