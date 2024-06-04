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
    modarr = sorted([(arr[i],i) for i in range(n)])

    for i in range(n//2):
        print(modarr[i][1]+1,modarr[n-i-1][1]+1)

for _ in range(1):
    solve()