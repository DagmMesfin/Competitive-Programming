class Solution(object):
    def minAddToMakeValid(self, s):
        stk = []
        for i in s:
            if not stk:
                stk.append(i)
            elif stk[-1] == "(" and i == ")":
                stk.pop()
            else:
                stk.append(i)
        return len(stk)
        