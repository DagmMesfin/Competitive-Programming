class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sum, prevsum = 0, 0
        CrSt = set()
        for num in nums:
            sum = (sum+num)%k
            if sum in CrSt:
                return True
            CrSt.add(prevsum)
            prevsum = sum
        return False