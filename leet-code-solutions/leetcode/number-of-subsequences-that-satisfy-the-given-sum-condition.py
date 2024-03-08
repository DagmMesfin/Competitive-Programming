class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n=len(nums)
        sumo=0
        nums.sort()
        def search(mino):
            left = mino-1
            right = n
            while left+1 < right:
                mid = (left+right)//2
                if nums[mino]+nums[mid]<=target:
                    left = mid
                else:
                    right = mid
            return left if left >= mino else -1
        
        for i in range(n):
            l = i
            r = search(l)
            if r!=-1:
                sumo += pow(2,r-l)
                sumo%=((10**9)+7)

        return sumo


