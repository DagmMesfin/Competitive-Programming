class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        leno = 0
        sumo = 0
        for i in range(len(candidates)):
            sumo+=candidates[i]
            if sumo>=target:
                leno = i
                break
        for k in range(1,leno+2):
            subsets=[]
            def sub(i):
                if len(subsets)==k and sum(subsets) == target:
                    res.append(subsets.copy())
                    return
                if len(subsets) == k:
                    return
                if i>=len(candidates):
                    return
                if sum(subsets) < target:
                    subsets.append(candidates[i])
                    sub(i+1)
                    subsets.pop()

                while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                    i+=1
                sub(i+1)  
            sub(0)
        return res