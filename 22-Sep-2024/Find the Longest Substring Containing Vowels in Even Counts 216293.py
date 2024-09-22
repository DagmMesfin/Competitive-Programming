# Problem: Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        d = {0: -1}
        ans = 0
        cur = 0
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

        for i, c in enumerate(s):
            if c in vowels:
                cur ^= 1 << vowels[c]
            if cur not in d:
                d[cur] = i
            ans = max(ans, i - d[cur]) 
            
        return ans