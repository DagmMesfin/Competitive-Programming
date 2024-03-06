class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        def isinit(nums,isinverse):
            n = len(nums)
            l,h = 0,n-1
            mid = (l+h)//2
            if n == 0:
                return -1
            if not isinverse:
                while l+1<h:
                    mid = (l+h)//2
                    if nums[mid] >= target:
                        h = mid
                    else:
                        l = mid
            else:
                while l+1<h:
                    mid = (l+h)//2
                    if nums[mid] <= target:
                        l = mid
                    else:
                        h = mid


            if not isinverse:
                if nums[l] == target:
                    return l
                elif nums[h] == target:
                    return h
            else:
                if nums[h] == target:
                    return h
                elif nums[l] == target:
                    return l
            return -1

        return [isinit(nums,False),isinit(nums,True)]
            
            