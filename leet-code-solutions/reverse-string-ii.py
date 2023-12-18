class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        stack = []
        for i in range(len(s)//(2*k)):
            stack.append(s[k-1::-1])
            stack.append(s[k:2*k])
            s = s[2*k:]
        if len(s) >= k:
            stack.append(s[k-1::-1])
            stack.append(s[k:])
            s = ""
        elif len(s) < k:
            stack.append(s[::-1])
            s = ""
        return "".join(stack)


