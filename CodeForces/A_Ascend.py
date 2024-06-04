from collections import deque
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
    arr = dmsllinp(int)
    monstk = []
    monstk.append(arr[0])
    leno = 1
    for i in range(1,n):
        if monstk and monstk[-1] >= arr[i]:
            monstk = []
        monstk.append(arr[i])
        leno = max(leno,len(monstk))
    return leno

for _ in range(1):
    print(solve())