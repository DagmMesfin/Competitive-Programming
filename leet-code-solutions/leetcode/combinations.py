class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        res=[]
        subsets=[]
        def sub(i):
            if len(subsets)==k:
                res.append(subsets.copy())
                return
            if i>=n:
                return
            subsets.append(nums[i])
            sub(i+1)
            subsets.pop()
            sub(i+1)
        
        sub(0)

        return res