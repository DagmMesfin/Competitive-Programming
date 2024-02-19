class Solution:
    def sortColors(self, nums: List[int]) -> None:
        dicto = {i:0 for i in range(3)}
        for i in range(len(nums)):
            dicto[nums[i]]+=1
        i = 0
        for j,k in dicto.items():
            for l in range(k):
                nums[i] = j
                i+=1
            
        
        