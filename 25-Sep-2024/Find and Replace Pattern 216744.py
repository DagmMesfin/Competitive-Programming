# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []

        for word in words:
            mapo1 = {}
            mapo2 = {}

            flag = 0

            for l,m in zip(word,pattern):
                if mapo1.get(m,l)==l and mapo2.get(l,m)==m:
                    mapo1[m] = l
                    mapo2[l] = m
                else:
                    flag = 1
                    break

            if not flag:
                ans.append(word)

        return ans