def dmslinp(datatype):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))
for _ in range(dmslinp(int)):
    a,b,c = dmsllinp(int)
    if a<b<c:
        print("STAIR")
    elif a<b>c:
        print("PEAK")
    else:
        print("NONE")