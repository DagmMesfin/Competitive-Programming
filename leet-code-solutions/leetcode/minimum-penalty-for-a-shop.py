class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefixN = [0]*(n+1)
        suffixY = [0]*(n+1)
        countN = 0
        countY = 0
        for i in range(n):
            if customers[i] == "N":
                countN+=1
            if customers[-1-i] == "Y":
                countY+=1
            prefixN[i+1] = countN
            suffixY[-2-i] = countY

        minindex = 0
        minPen = prefixN[0]+suffixY[0]
        for i in range(1,n+1):
            if prefixN[i]+suffixY[i] < minPen:
                minindex = i
                minPen = prefixN[i]+suffixY[i]
        return minindex

