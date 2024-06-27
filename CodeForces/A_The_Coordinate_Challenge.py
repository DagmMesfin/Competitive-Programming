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
    if n == 1: return 2
    if n == 2 or n == 3: return 1
    else: return ceil(n/3)

for _ in range(dmslinp(int)):
    print(solve())