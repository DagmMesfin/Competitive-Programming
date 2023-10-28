class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backtrack(opeN, closN):
            if opeN == closN == n:
                res.append("".join(stack))
                return
            if opeN < n:
                stack.append("(")
                backtrack(opeN+1, closN)
                stack.pop()
            if closN < opeN:
                stack.append(")")
                backtrack(opeN, closN+1)
                stack.pop()
        backtrack(0, 0)
        return res
