from collections import Counter
import sys
input = lambda: sys.stdin.readline().strip()
def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    n = dmslinp(int)
    arro = dmsllinp(int)
    
    counto = Counter(arro)
    maxo = max(counto.keys())
    memo = {} 

    def dp(i):

        if i <= 1:
            return counto[i]
        
        if i not in memo:
            memo[i] = max(dp(i-1),dp(i-2),counto[i]*i)
        
        return memo[i]
    
    return dp(maxo)
    


for _ in range(1):
    print(solve())