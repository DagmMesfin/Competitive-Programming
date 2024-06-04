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
    password = dmslinp()
    monstk = []
    
    for val in password:
        if monstk:
            if monstk[-1].isalpha() and monstk[-1] <= val:
                monstk.append(val)
            elif not monstk[-1].isalpha() and monstk[-1] <= val:
                monstk.append(val)
        else:
            monstk.append(val)
    
    return "YES" if len(monstk) == n else "NO"

for _ in range(dmslinp(int)):
    print(solve())