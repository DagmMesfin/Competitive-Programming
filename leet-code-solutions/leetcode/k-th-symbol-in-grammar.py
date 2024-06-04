class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        mid_len = 2**(n-1)//2
        if k<=mid_len:
            return self.kthGrammar(n-1,k)
        else:
            return (self.kthGrammar(n-1,k-mid_len)+1)%2
