from heapq import heappush
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
    a = dmsllinp(int)
    b = dmsllinp(int)
    ops = 0
    diff = []
    done = 0
    for i in range(n):
        ops += abs(a[i]-b[i])
        if not done and ((a[i] >= b[-1] >= b[i]) or (a[i]<= b[-1] <=b[i])):
            done = 1
            ops+=1
        else:
            heappush(diff,abs(a[i]-b[-1]))
            heappush(diff,abs(b[i]-b[-1]))


    return ops if done else ops+diff[0]+1
    


for _ in range(dmslinp(int)):
    print(solve())