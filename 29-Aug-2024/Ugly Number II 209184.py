# Problem: Ugly Number II - https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0
        while len(ugly) < n:
            nm2 = ugly[i2] * 2
            nm3 = ugly[i3] * 3
            nm5 = ugly[i5] * 5

            nxtu = min(nm2, nm3, nm5)

            ugly.append(nxtu)

            if nxtu == nm2:
                i2 += 1
            if nxtu == nm3:
                i3 += 1
            if nxtu == nm5:
                i5 += 1

        return ugly[n - 1]