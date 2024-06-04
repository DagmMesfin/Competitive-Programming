class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        arr = [""]*len(s)
        for j,i in enumerate(indices):
            arr[i] = s[j]
        return "".join(arr)