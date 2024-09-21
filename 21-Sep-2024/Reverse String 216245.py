# Problem: Reverse String - https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def rev(i):
            if i == len(s)//2:
                return
            s[len(s)-i-1],s[i] = s[i],s[len(s)-i-1]
            rev(i+1)
        rev(0)
        
            