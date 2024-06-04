class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        pre_up_sum = [0]*n
        for l,r,up in bookings:
            pre_up_sum[l-1]+=up
            if r < n:
                pre_up_sum[r]-=up

        for i in range(n-1):
            pre_up_sum[i+1] = pre_up_sum[i]+pre_up_sum[i+1]
        
        return pre_up_sum





        