from math import gcd


def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    n,k = dmsllinp(int)
    listo = dmsllinp(int)
    mino = min(listo)
    maxo = max(listo)
    gcdo = listo[0]-k
    count = 0
    if len(set(listo)) == 1:
        return 0
    if mino<=k<=maxo:
        return -1
    for i in range(n):
        listo[i]-=k
        gcdo = gcd(listo[i],gcdo)
    for i in range(n):
        count+=abs((listo[i])//gcdo)-1
    return count


for _ in range(dmslinp(int)):
    print(solve())



