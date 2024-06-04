def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    n,z = dmsllinp(int)
    arro = dmsllinp(int)
    maxval = 0

    for i in range(n):
        maxval = max(maxval,arro[i] | z)
    
    return maxval



for _ in range(dmslinp(int)):
    print(solve())