from math import ceil
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
    ans = [1]*n

    for i in range(1,n):
        
        ans[i]+=ans[i-1] + ((i+1)//2 - 1)
    print(ans)
    
    return ans[-1]


for _ in range(dmslinp(int)):
    print(solve())