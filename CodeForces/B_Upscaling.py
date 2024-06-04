def dmslinp(datatype):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))

for _ in range(dmslinp(int)):
    n = dmslinp(int)
    points = ["#","."]
    res = []
    for i in range(n):
        listo = []
        for j in range(n):
            listo.append(points[(j%2 + i%2)%2]*2)
        print("".join(listo))
        print("".join(listo))
    