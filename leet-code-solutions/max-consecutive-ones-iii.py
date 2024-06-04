class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        dicto = defaultdict(int)
        maxo =0
        l = 0

        for i in range(len(nums)):
            dicto[nums[i]] += 1

            while (dicto[0] > k) and l<=i:
                dicto[nums[l]]-=1
                l+=1
            
            maxo = max(maxo, i-l+1)

        return maxo
            