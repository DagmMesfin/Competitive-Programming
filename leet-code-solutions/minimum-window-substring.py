class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        def comparator(c1,c2):
            for keys in c1:
                if c2[keys] < c1[keys]:
                    return False
            return True

        lenS=len(s)
        lenT=len(t)
        countT = Counter(t)
        countS = Counter()
        matches = 0
        ans = ''
        mino = float('inf')
        lf = 0
        rf = 0
        l = 0
        for r in range(lenS):
            countS[s[r]]+=1
            leno = r-l+1
            while comparator(countT,countS):
                mino = min(mino,leno)
                if mino == leno:
                    lf = l
                    rf = r
                countS[s[l]] -= 1
                l += 1
                leno = r-l+1
                
        return s[lf:rf+1] if mino != float("inf") else ''
        