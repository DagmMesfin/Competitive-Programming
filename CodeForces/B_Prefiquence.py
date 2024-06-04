def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    n,m = dmsllinp(int)
    a = dmslinp()
    b = dmslinp()

    i = 0

    for j in range(m):
        if a[i] == b[j]:
            i+=1
        if i >= n:
            break

        
    return(i)
        

for _ in range(dmslinp(int)):
    print(solve())