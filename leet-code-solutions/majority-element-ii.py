class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        limit = len(nums)//3
        result = []
        uniquenumbers = set(nums)
        for number in uniquenumbers:
            if nums.count(number) > limit:
                result.append(number)
        return result