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
    x,y= dmsllinp(int)
    
    if y//2:
        return max(ceil(y/2)+ceil(x/7))
    else:
        if y == 0:
            return ceil(x/15)
        else:
            return ceil(x/11)

for _ in range(dmslinp(int)):
    print(solve())