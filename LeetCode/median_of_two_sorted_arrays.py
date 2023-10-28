class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedlist = []
        med = 0
        for j in range(len(nums2)):
            mergedlist.append(nums2[j])
        for i in range(len(nums1)):
             mergedlist.append(nums1[i])
        mergedlist.sort()
        if(len(mergedlist)%2==0):
            med = (mergedlist[int((len(mergedlist)/2)-1)] + mergedlist[int((len(mergedlist)/2))])/2
        else:
            med = mergedlist[int((len(mergedlist)/2))]
        return med
        