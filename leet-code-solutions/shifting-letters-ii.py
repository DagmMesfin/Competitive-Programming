class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        stacko = []
        pre_up_sum = [0]*n
        for l,r,dire in shifts:
            up = -1 if dire == 0 else 1
            pre_up_sum[l]+=up
            if r+1 < n:
                pre_up_sum[r+1]-=up

        for i in range(n-1):
            pre_up_sum[i+1] = pre_up_sum[i]+pre_up_sum[i+1]

        for j,sumo in enumerate(pre_up_sum):
            numo = ord(s[j])-ord('a')
            stacko.append(chr(ord('a') + (numo+sumo)%26))
        
        return ''.join(stacko)