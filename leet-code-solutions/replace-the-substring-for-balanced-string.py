class Solution:
    def balancedString(self, s: str) -> int:
        def comp(temp, off):
            for i in "QWER":
                if temp[i] > off[i]:
                    return False
            return True
        
        temp_dicto = {i:(0-len(s)//4) for i in "QWER"}
        offseto = {i: 0 for i in "QWER"}

        for i in s:
            temp_dicto[i]+=1
        win  = len(s)
        l=0

        if comp(temp_dicto,  offseto):
            return 0

        for r in range(len(s)):
            offseto[s[r]] += 1
            while comp(temp_dicto,  offseto) and l <= r:
                offseto[s[l]] -= 1
                win = min(win, r-l+1)
                l+=1
        
        return win


                

             
