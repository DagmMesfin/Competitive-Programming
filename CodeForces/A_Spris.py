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
    a = dmslinp(int)
    b = dmslinp(int)
    c = dmslinp(int)

    ratio = min(c//4,b//2,a)

    return ratio*(7)



for _ in range(1):
    print(solve())