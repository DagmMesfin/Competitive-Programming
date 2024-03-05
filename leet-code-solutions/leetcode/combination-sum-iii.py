class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [i for i in range(1,10)]
        res=[]
        subsets=[]
        def sub(i):
            if len(subsets)==k and sum(subsets) == n:
                res.append(subsets.copy())
                return
            if len(subsets) == k:
                return
            if i>=len(candidates):
                return
            if sum(subsets) < n:
                subsets.append(candidates[i])
                sub(i+1)
                subsets.pop()
                sub(i+1)  
        sub(0)
        return res