class Solution:
    def totalMoney(self, n: int) -> int:
        m = 0
        for i in range(1, n+1):
            m+=i%7+((i)//7)
            if i%7 == 0:
                m+=6
        return m