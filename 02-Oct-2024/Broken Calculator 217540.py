# Problem: Broken Calculator - https://leetcode.com/problems/broken-calculator/description/

class Solution:
    def brokenCalc(self, st: int, target: int) -> int:
        step = 0
        while target>st:
            if not target%2:
                target//=2
            else:
                target+=1
            step+=1
        return step + abs(target-st)


        