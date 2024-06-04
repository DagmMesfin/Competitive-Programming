class Solution:
    def minimizedStringLength(self, s: str) -> int:
        minLenSet = set()
        for i in s:
            minLenSet.add(i)
        return len(minLenSet)
