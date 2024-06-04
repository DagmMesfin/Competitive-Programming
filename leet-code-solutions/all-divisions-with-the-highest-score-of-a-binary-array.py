class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dicto = defaultdict(list)
        high_divscore = 0
        leno = len(nums)

        sum_left = [0] * (leno+1)
        left_keep = 0
        sum_right = [0] * (leno+1)
        right_keep=0

        #building up a prefix sum for the right and left elements
        for i in range(leno):
            if nums[i] == 0:
                left_keep += 1
            if nums[-1-i] == 1:
                right_keep += 1
            sum_left[i+1] = left_keep
            sum_right[-i-2] = right_keep
        
        #traversing through the division sum and keep the highest while keeping the index in dictionary
        for i in range(leno+1):
            div_sum = sum_left[i]+sum_right[i]
            dicto[div_sum].append(i)
            high_divscore = max(high_divscore, div_sum)
        
        return dicto[high_divscore]

        

