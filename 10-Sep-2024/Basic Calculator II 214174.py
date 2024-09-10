# Problem: Basic Calculator II - https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        cur_res = 0
        last_op = '+'
        numo = 0
        ans = 0

        for x in s+'+':
            if x.isdigit():
                numo = numo * 10 + int(x)

            if x in ('+', '-', '/', '*'):
                if last_op == '+':
                    cur_res += numo
                elif last_op == '-':
                    cur_res -= numo
                elif last_op == '*':
                    cur_res *= numo
                elif last_op == '/':
                    cur_res = int(cur_res/numo)
                
                if x in ('+', '-'):
                    ans += cur_res
                    cur_res = 0
                
                last_op = x
                numo = 0
        
        return ans