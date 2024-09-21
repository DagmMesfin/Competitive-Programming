# Problem: D - Maximum Number of Zeroes - https://codeforces.com/gym/514644/problem/D

from collections import defaultdict
from math import gcd
def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))

def solve():
    n = dmslinp(int)
    a = dmsllinp(int)
    b = dmsllinp(int)
    counter = defaultdict(int)
    anycount = 0
    for i in range(n):
        if a[i] == 0:
            if b[i] == 0:
                anycount += 1
        else:
            numo = gcd(a[i],b[i])
            nult = 1
            if a[i]*b[i] < 0:
                nult = -1
            upper = nult*abs(a[i]//numo)
            lower = abs(b[i]//numo)
            counter[(upper,lower)] += 1
    
    if not counter:
        return anycount
    else:
        return max(counter.values())+anycount
    
            
for _ in range(1):
    print(solve())