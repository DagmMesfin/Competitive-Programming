class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        counter = 0
        maxico = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in range(k):
            if s[i] in vowels:
                counter += 1
        maxico = max(maxico, counter)
        for i in range(1, len(s) - k + 1):
            counter -= 1 if s[i-1] in vowels else 0
            counter += 1 if s[i+k-1] in vowels else 0
            maxico = max(maxico, counter)
        return maxico