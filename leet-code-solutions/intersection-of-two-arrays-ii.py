class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        res = []

        for i,j in count1.items():
            j = min(j,count2.get(i, 0))
            res.extend([i for k in range(j)])
            
        return res

