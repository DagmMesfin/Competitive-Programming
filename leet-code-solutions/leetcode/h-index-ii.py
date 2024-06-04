class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        left,right = -1, n
        while left+1 < right:
            mid = (left+right)//2
            if citations[mid] - (n-1-mid) > 0:
                right = mid
            else:
                left = mid
        return n-right
