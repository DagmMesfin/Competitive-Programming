class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        prev = 0
        maxo = 0
        partition = []
        last = dict()
        n = len(s)
        for i in range(n):
            last[s[i]] = i
        
        for i in range(n):
            letter = s[i]
            maxo = max(maxo,last[letter])
            if maxo == i:
                partition.append(maxo-prev + 1)
                prev = maxo + 1
        return partition

        
        

        