class Solution(object):
    def evalRPN(self, tokens):
        opr = ["+", "-", "/", "*"]
        stack = []
        def Operate(oper, a, b):
            if oper == "+":
                return a+b
            elif oper == "-":
                return a-b
            elif oper == "*":
                return a*b
            elif oper == "/":
                return a//b if a*b >= 0 else int(-1*floor(-1*a/b))
        
        for i in tokens:
            if i in opr:
                val = Operate(i, stack[-2], stack[-1])
                stack[:] = stack[:-2]
                stack.append(val)
            else:
                stack.append(int(i))
        return stack[0]
        