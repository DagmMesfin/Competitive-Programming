class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        s = list(s.split())
        return ' '.join(s[::-1])