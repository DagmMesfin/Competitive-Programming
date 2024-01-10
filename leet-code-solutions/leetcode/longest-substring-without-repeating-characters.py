class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = set()
        left, right = 0, 0
        max_len = 0

        while right < len(s):
            if s[right] not in res:
                res.add(s[right])
                max_len = max(max_len, right - left + 1)
                right+=1
            else:
                res.remove(s[left])
                left+=1
        return max_len
        