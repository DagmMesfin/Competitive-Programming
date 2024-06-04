def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    h,w = dmsllinp(int)
    matrix = []
    def inbound(i,j):
        return 0<=i<h and 0<=j<w
    directions = [(0,1),(0,-1),(1,0)]
    for _ in range(h):
        listo = dmslsplit(input())
        matrix.append(listo)
    print(matrix)




for _ in range(1):
    print(solve())