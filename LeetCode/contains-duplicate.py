class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        CrSt = set()
        numstr = []
        isthere = False
        for st in nums:
            if st in CrSt:
                isthere = True
                break
            CrSt.add(st)
        return isthere
