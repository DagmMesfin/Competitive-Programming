class Solution(object):
    def fib(self, n):
        fibbo = [0,1]
        if n == 1 or n == 0:
            return n
        else:
            for i in range(2,n+1):
                numo = fibbo[i-1] + fibbo[i-2]
                fibbo.append(numo)
            return fibbo[-1]

        