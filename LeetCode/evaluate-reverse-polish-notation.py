class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opr = ["+", "-", "/", "*"]
        stack = []
        def Operate(oper, a, b) -> int:
            if oper == "+":
                return a+b
            elif oper == "-":
                return a-b
            elif oper == "*":
                return a*b
            elif oper == "/":
                return int(a/b)
        
        for i in tokens:
            if i in opr:
                val = Operate(i, stack[-2], stack[-1])
                stack[:] = stack[:-2]
                stack.append(val)
            else:
                stack.append(int(i))
        return stack[0]