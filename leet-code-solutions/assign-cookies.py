class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        slen = len(s)
        glen = len(g)
        i = 0
        j = 0
        counter = 0

        for j in range(slen):
            if i==glen:
                break
            if g[i] <= s[j]:
                i+=1
                counter+=1
        
        return counter