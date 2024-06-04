from math import gcd, lcm
def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    n = dmslinp(int)
    arro = dmsllinp(int)
    res_lcm = [0 for _ in range(n+1)]
    res_lcm[0] = arro[0]
    res_lcm[-1] = arro[-1]
    for i in range(1,n):
        res_lcm[i] = lcm(arro[i],arro[i-1])
    constr = []

    for i in range(1,n+1):
        constr.append(gcd(res_lcm[i],res_lcm[i-1]))

    if arro == constr:
        return "YES"
    else:
        return "NO"
        

for _ in range(dmslinp(int)):
    print(solve())