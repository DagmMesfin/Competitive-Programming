class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        i = 0
        maxque = deque()
        minque = deque()
        maxsize = 0

        for r in range(len(nums)):
            while maxque and nums[r] > maxque[-1]:
                maxque.pop()
            while minque and nums[r] < minque[-1]:
                minque.pop()

            maxque.append(nums[r])
            minque.append(nums[r])

            if maxque[0] - minque[0] > limit:
                if maxque[0] == nums[i]:
                    maxque.popleft()
                if minque[0] == nums[i]:
                    minque.popleft()
                i+=1
            maxsize = max(maxsize,r-i+1)

        return maxsize