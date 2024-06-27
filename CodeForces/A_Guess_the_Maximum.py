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
    maxo = float("inf")
    for i in range(n-1):
        maxo = min(maxo,max(arr[i],arr[i+1]))
    
    return maxo-1

for _ in range(dmslinp(int)):
    print(solve())