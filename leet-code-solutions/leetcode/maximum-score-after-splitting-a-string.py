class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        score = 0
        leftsum = [0]*n
        rightsum = [0]*n
        countleft = 0
        countright = 0

        for i in range(n):
            if s[i] == "0":
                countleft+=1
            if s[-1-i] == "1":
                countright+=1
            leftsum[i] = countleft
            rightsum[-1-i] = countright

        for i in range(n-1):
            score = max(score,leftsum[i]+rightsum[i+1])

        return score
            
                

        
        