class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        count = 0
        oddCount = 0

        for r in range(len(nums)):
            oddCount+=1 if nums[r]%2!=0 else 0
    
            if oddCount==k:
                leftSido = 1
                rightSido = 1
                while nums[l]%2==0:
                    l+=1
                    leftSido+=1
                l+=1
                tempRight = r+1
                while tempRight < len(nums) and nums[tempRight]%2 == 0:
                    tempRight+=1
                    rightSido += 1
                oddCount-=1
                count+=(leftSido*rightSido)
        return count
