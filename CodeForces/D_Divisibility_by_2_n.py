from math import log
from math import ceil, floor
import sys
input = sys.stdin.readline
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
    counter = 0
    arro=[]
    counter = 0
    for num in arr:
        d = 2
        while d*d <= num:
            while num%d == 0:
                arro.append(d)
                num//=d
            d+=1
        if num>1:
            arro.append(num)
    counter = arro.count(2)
    req = n
    rem = floor(log(n,2))
    keep = req-counter
    cost = 0
    if (rem*(rem+1))//2 < keep:
        return -1
    
    while keep:
        keep-=rem
        rem-=1
        cost += 1
    
    return cost

for _ in range(dmslinp(int)):
    print(solve())