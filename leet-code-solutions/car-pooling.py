class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        maxo = 0
        mino = float('inf')
        for up,l,r in trips:
            maxo = max(maxo,r)
        n = maxo+1
        pre_up_sum = [0]*n
        for up,l,r in trips:
            pre_up_sum[l]+=up
            if r < n:
                pre_up_sum[r]-=up

        for i in range(n):
            pre_up_sum[i] += pre_up_sum[i-1] if i>0 else 0
            if pre_up_sum[i] > capacity:
                return False
        return True
        