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
    n,m  =dmsllinp(int)
    hb = dmsllinp(int)
    hg = dmsllinp(int)
    nb = hb[0]
    ng = hg[0]
    hb = set(hb[1:])
    hg = set(hg[1:])
    


for _ in range(1):
    print(solve())