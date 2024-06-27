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
    n,k = dmsllinp(int)
    arr = dmsllinp(int)
    maxo = max(arr)
    opers = []
    arr.append(0)

    for i in range(n):
        opers.append(arr[i+1]-arr[i]-k if arr[i+1]>=arr[i] else 0)
    
    for i in range(n):
        if opers[i] < 0:
            opers[i] = arr[i]+1
        else:
            opers[i] = 0

    ano = max(opers)

    return max(maxo,ano)


for _ in range(dmslinp(int)):
    print(solve())