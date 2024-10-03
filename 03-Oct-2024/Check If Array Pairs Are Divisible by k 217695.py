# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        dicto = defaultdict(int)
        for x in arr:
            dicto[x%k] += 1

        for i in range(k):
            if i*2 == k:
                if dicto[i]%2:
                    return False
            else:
                if dicto[i] != dicto[(k-i)%k]:
                    return False
        
        return True



