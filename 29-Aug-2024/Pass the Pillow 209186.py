# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        dire = 1
        init = 1
        while time:
            init+=dire
            time-=1
            if init == n or init == 1:
                dire*=-1
        return init
            

