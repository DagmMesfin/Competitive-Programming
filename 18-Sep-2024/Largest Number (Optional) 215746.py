# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        dicto = defaultdict(list)

        for i in range(len(nums)):
            nums[i] = str(nums[i])
            dicto[int(nums[i][0])].append(nums[i])

        ans = []

        for i in range(9,-1,-1):
            arro = dicto[i]
            for j in range(len(arro)-1):
                for k in range(len(arro)-j-1):
                    one = int(arro[k] + arro[k+1])
                    two = int(arro[k+1] + arro[k])
                    if one < two:
                        arro[k],arro[k+1] = arro[k+1],arro[k]
            ans.extend(arro)
            
        return "".join(ans).lstrip("0") or "0" 