class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n2 = len(nums2)
        monStk = []
        res = []
        ans = [-1] * n2
        dicto = defaultdict(int)

        for i in range(n2):
            while monStk and nums2[monStk[-1]] < nums2[i]:
                ans[monStk.pop()] = i
            monStk.append(i)

        for i in range(n2):
            dicto[nums2[i]] = ans[i]

        for num in nums1:
            res.append(nums2[dicto[num]]) if dicto[num] != -1 else res.append(dicto[num])
            
        return res


        