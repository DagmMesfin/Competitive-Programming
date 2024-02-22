class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk = []
        for log in logs:
            if log == './':
                continue
            if log == '../':
                if stk:
                    stk.pop()
            else:
                stk.append(log)
        return len(stk)