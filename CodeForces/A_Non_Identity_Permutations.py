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
    arr = [i for i in range(n,0,-1)]
    if n%2:
        arr[n//2],arr[-1] = arr[-1],arr[n//2]
    return arr

for _ in range(dmslinp(int)):
    print(*solve())