from math import gcd


def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    x = dmslinp(int)
    ans = 0
    res = 0
    for y in range(1,x):
        temp = gcd(x,y)+y
        if temp > ans:
            ans = temp
            res = y
    return res

for _ in range(dmslinp(int)):
    print(solve())