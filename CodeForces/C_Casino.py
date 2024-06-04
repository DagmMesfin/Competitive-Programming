import sys
input = sys.stdin.readline
def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
def lcm(a,b):
    return a*b//gcd(a,b)

def solve():
    n = dmslinp(int)
    listo = dmsllinp(int)
    listo.sort()
    mino = listo[0]
    gcfo = gcd(mino,mino)
    for i in range(1,n):
        if listo[i]%gcfo:
            gcfo = gcd(gcfo,listo[i])
    for i in range(n):
        numo = listo[i]//gcfo
        while numo%2 == 0:
            numo//=2
        while not numo%3:
            numo//=3
        if numo!=1:
            return "No"
    return "Yes"
            
for _ in range(1):
    print(solve())