class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        res = []
        for i in range(len(nums)):
            if nums[i]<0:
                neg.append(nums[i])
            elif nums[i]>0:
                pos.append(nums[i])
        k = 0
        l = 0
        for j in range(len(nums)):
            if j%2 == 0:
                res.append(pos[k])
                k = k+1
            else:
                res.append(neg[l])
                l = l+1

        return res