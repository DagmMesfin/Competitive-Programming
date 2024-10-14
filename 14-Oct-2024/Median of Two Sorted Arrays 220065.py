# Problem: Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merger = []
        med = 0
        for j in range(len(nums2)):
            merger.append(nums2[j])
        for i in range(len(nums1)):
             merger.append(nums1[i])
        merger.sort()
        if(len(merger)%2==0):
            return (merger[int((len(merger)/2)-1)] + merger[int((len(merger)/2))])/2
        else:
            return merger[int((len(merger)/2))]
        # return med