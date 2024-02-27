class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def helper(l,r):
            if l == r:
                return nums[l]
            return max(nums[l] - helper(l+1,r), nums[r] - helper(l,r-1))
        testo = helper(0,len(nums)-1)
        if testo<0:
            return False
        return True
        