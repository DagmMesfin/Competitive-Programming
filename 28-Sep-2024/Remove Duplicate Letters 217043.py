# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution(object):
    def removeDuplicateLetters(self, s):
        s = list(s)
        stack = []
        seen = set()
        last_oc = {c:i for i,c in enumerate(s)}

        for idx,letter in enumerate(s):
            if letter not in seen:
                while stack and letter < stack[-1] and idx<last_oc[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(letter)
                stack.append(letter)
        
        return ''.join(stack)
        