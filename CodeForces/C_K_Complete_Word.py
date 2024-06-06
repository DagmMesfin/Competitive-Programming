from collections import defaultdict
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
    n,k = dmsllinp(int)
    s = dmslinp()

    steps = n//k
    cost = 0
    for i in range(k//2):
        count = defaultdict(int)
        pos = i
        negpos = n-i-1
        while pos < n:
            count[s[pos]]+=1
            pos+=k
        while negpos >= 0:
            count[s[negpos]]+=1
            negpos-=k
  
        cost += (steps*2 - max(count.values()))
    
    if k%2:
        count = defaultdict(int)
        pos = k//2
        while pos < n:
            count[s[pos]]+=1
            pos+=k

        cost += (steps - max(count.values()))

    return cost
        



for _ in range(dmslinp(int)):
    print(solve())