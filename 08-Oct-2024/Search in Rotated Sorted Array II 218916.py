# Problem: Search in Rotated Sorted Array II - https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def searchbinary(nums,target):
            l,h = 0,len(nums)-1

            while l<=h:
                mid = (l+h)//2
                if target > nums[mid]:
                    l = mid+1
                elif target < nums[mid]:
                    h = mid-1
                else:
                    return True
            return False

        return searchbinary(sorted(nums),target)