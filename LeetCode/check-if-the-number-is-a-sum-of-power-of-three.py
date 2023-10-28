class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        ispower = True
        if n>0:
            while n != 1:
                if n%3 == 2:
                    ispower = False
                    break
                n = (n - (n%3)) / 3
        else:
            ispower = False
        return ispower
