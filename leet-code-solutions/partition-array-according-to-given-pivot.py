class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equal = []
        more = []
        for i in range(len(nums)):
            if nums[i]>pivot:
                more.append(nums[i])
            elif nums[i] == pivot:
                equal.append(nums[i])
            else:
                less.append(nums[i])
        less.extend(equal)
        less.extend(more)
        
        return less

        