# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        alpha = Counter(word)
        alphacount = sorted(list(alpha.values()), reverse = True)
        count = 0

        j = 0
        k = 1
        for i in alphacount:
            count += i*k
            j+=1
            if not j%8:
                k+=1
        

        return count
        