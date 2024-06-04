class Solution(object):
    def isValid(self, s):
        close_open = {
            ')' : '(',
            ']' : '[',
            '}' : '{',
        }
        closers = [')', ']', '}']
        stack = []
        for i in range(len(s)):
            if stack and s[i] in closers and close_open[s[i]] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        return not stack
