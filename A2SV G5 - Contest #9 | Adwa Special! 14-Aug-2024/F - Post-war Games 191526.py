# Problem: F - Post-war Games - https://codeforces.com/gym/513152/problem/F

def dmslinp(datatype):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))

def solved():
    n,k = dmsllinp(int)
    if k==n:
        return 0
    return (n-(k+1))*3 + ((k-1)//2)*3 + (k+1)%2 + 1
for _ in range(dmslinp(int)):
    print(solved())
    

