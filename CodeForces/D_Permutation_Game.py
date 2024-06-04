def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    n,k,sta,stp = dmsllinp(int)
    perm = dmsllinp(int)
    a = dmsllinp(int)
    

for _ in range(dmslinp(int)):
    print(solve())