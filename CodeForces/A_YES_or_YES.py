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
    yes = [("Y",'y'),("E",'e'),("S",'s')]
    s = dmslinp()
    for i in range(3):
        if s[i] not in yes[i]:
            return "NO"
    return "YES"


for _ in range(dmslinp(int)):
    print(solve())