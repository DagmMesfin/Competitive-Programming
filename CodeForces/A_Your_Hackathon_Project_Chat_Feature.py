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
    s = dmslinp()
    endo = 0

    for i in range(n):
        if s[i] == ")":
            endo+=1
        else:
            endo = 0
    
    return "Yes" if endo > n-endo else "No" 
        


for _ in range(dmslinp(int)):
    print(solve())