class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(mid):
            capacity = mid
            dday = 1

            for weight in weights:
                if capacity - weight >= 0:
                    capacity -= weight
                else:
                    dday+=1
                    capacity = mid-weight


            return dday <= days

        
        left = max(weights)
        right = sum(weights)

        while left+1 < right:
            mid = (left+right)//2
            if possible(mid):
                right = mid
            else:
                left = mid
            
        if possible(left):
            return left
        else:
            return right
        
                     
