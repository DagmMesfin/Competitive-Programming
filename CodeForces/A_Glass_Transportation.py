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
    n,m = dmsllinp(int)
    arr = dmsllinp(int)
    for i in range(n):
        arr[i] *= arr[i]
    arr.sort() 
    glass = []
    for _ in range(m):
        a,b = dmsllinp(int)
        glass.append(a*a + b*b)
    glass.sort()

    i = 0
    j = 0

    while i<n and j<m:
        if glass[j] <= arr[i]:
            i+=1
            j+=1
        else:
            i+=1
    
    return j
    

for _ in range(dmslinp(int)):
    print(solve())