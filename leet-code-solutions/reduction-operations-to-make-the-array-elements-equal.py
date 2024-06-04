class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        dicto = Counter(nums)
        nums = sorted(list(set(nums)))
        counter = 0
        for i,numo in enumerate(nums):
            counter += i*dicto[numo]
        return counter