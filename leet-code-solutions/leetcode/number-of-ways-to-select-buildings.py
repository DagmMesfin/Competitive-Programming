class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        n0_pre = [0]*n
        n1_pre = [0]*n
        n01_pre = [0]*n
        n10_pre = [0]*n
        n010_pre = [0]*n
        n101_pre = [0]*n

        

        sumo0 = 0
        sumo1 = 0

        for i in range(n):
            if s[i] == '0':
                sumo0+=1
            if s[i] == '1':
                sumo1+=1
            n0_pre[i] = sumo0
            n1_pre[i] = sumo1
            if i>0:
                if s[i] == '0':
                    n01_pre[i] = n01_pre[i-1]
                    n10_pre[i] = n10_pre[i-1] + n1_pre[i-1]
                    n010_pre[i] = n010_pre[i-1] + n01_pre[i-1]
                    n101_pre[i] = n101_pre[i-1]
                if s[i] == '1':
                    n01_pre[i] = n01_pre[i-1] + n0_pre[i-1]
                    n10_pre[i] = n10_pre[i-1]
            if i>1:
                if s[i] == '0':
                    n010_pre[i] = n010_pre[i-1] + n01_pre[i-1]
                    n101_pre[i] = n101_pre[i-1]
                if s[i] == '1':
                    n010_pre[i] = n010_pre[i-1]
                    n101_pre[i] = n101_pre[i-1] + n10_pre[i-1]

        return n010_pre[-1] + n101_pre[-1]
        
        

