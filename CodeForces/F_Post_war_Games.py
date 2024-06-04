def dmslinp(datatype):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


for _ in range(int(input())):
    n,k = map(int,input().split())
    if k==n:
        print(0)
    else:
        print((n-(k+1))*3 + ((k-1)//2)*3 + (k+1)%2 + 1)
    

