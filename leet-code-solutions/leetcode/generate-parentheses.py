class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def bracketter(opener, closer):
            if opener == closer == n:
                res.append("".join(stack))
                return
            if opener < n:
                stack.append("(")
                bracketter(opener+1, closer)
                stack.pop()
            if closer < opener:
                stack.append(")")
                bracketter(opener, closer+1)
                stack.pop()
        bracketter(0, 0)
        return res