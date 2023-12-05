class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        #sort the number of sides
        nums.sort(reverse = True)
        maxtotal = 0

        for i in range(len(nums)-2):
            a = nums[i]
            b = nums[i+1]
            c = nums[i+2]
            #check for the conditions of a triangle
            if not (a+b>c and b+c>a and c+a>b):
                continue
            #update the maximum perimeter
            maxtotal = max(maxtotal, a+b+c)

        return maxtotal