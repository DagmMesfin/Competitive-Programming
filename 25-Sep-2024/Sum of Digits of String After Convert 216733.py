# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = [ord(ele) - ord("a") + 1 for ele in s]
        cur = ""
        for i in num:
            cur += str(i)
        cur = int(cur)
        transform = lambda x : sum(list(map(int,str(x))))

        for i in range(k):
            cur = transform(cur)
        return cur