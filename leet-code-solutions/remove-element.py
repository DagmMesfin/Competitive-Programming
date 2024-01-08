class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        stack = []
        for num in nums:
            if num != val:
                stack.append(num)
        nums[:] = stack[:]
        return len(stack)