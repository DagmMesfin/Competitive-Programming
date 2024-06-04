class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stk = []
        numo = 0
        score = 0
        for i in s:
            if i == "(":
                stk.append(0)
            else:
                val = stk.pop()
                if val == 0:
                    numo = 1
                else:
                    numo = val * 2
                
                if not stk:
                    score += numo
                else:
                    stk[-1] += numo
        return score