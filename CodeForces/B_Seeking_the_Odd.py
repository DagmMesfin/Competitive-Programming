def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))

def solve():
    n = dmslinp(int)
    if n%2:
        return "YES"
    else:
        while not n%2:
            n//=2
        if n==1:
            return "NO"
        return "YES"


for _ in range(dmslinp(int)):
    print(solve())