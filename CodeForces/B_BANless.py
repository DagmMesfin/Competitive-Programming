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
    n  = dmslinp(int)
    s2s = ceil(n/2)
    ans = []

    for i in range(0,s2s):
        ans.append([i*3+1,3*n - 3*(i)])
    
    print(s2s)

    for i in range(s2s):
        print(*ans[i])
    
    


for _ in range(dmslinp(int)):
    solve()