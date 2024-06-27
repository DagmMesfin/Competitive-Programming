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
    x,y = dmsllinp(int)
    xrax = x^y  
        
    twcom = -xrax               
    rms = xrax & twcom 

    return rms


for _ in range(dmslinp(int)):
    print(solve())