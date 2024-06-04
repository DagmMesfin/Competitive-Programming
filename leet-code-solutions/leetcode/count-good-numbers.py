class Solution:
    def countGoodNumbers(self, n: int) -> int:
        m = (n + 1)//2
        k = n//2
        mod = 1000000007
        return (pow(5,m,mod)*pow(4,k,mod))%mod