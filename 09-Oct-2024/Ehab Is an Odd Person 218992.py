# Problem: Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

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
    isdiff = False
    for i in range(n-1):
        if arr[i]%2 != arr[i+1]%2:
            isdiff = True
            break
    
    if isdiff:
        arr.sort()


    
    return arr


for _ in range(1):
    print(*solve())