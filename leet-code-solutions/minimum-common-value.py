class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = set(nums1)
        nums2 = set(nums2)

        inter = sorted(list(nums1.intersection(nums2)))

        return inter[0] if inter else -1
