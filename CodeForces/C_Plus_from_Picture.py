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
    countcross = 0
    countpoint = 0
    points = []
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    def inbound(i,j):
        return 0<=i<h and 0<=j<w
    def up(i,j):
        return inbound(i+1,j) and matrix[i+1][j] == "*"
    def down(i,j):
        return inbound(i-1,j) and matrix[i-1][j] == "*"
    def left(i,j):
        return inbound(i,j-1) and matrix[i][j-1] == "*"
    def right(i,j):
        return inbound(i,j+1) and matrix[i][j+1] == "*"
    def checko(i,j):
        return matrix[i][j] == "*" and up(i,j) and down(i,j) and left(i,j) and right(i,j)
    
    for i in range(h):
        listo = dmslsplit(input(),str,list)
        countcross+=listo.count("*")
        matrix.append(listo)
    for i in range(h):
        for j in range(w):
            if checko(i,j):
                countpoint+=1
                points.append((i,j))

    if countpoint == 0 or countpoint >1:
        return "NO"
    k,m = points[0]

    for i in range(4):
        x,y = directions[i]
        newx,newy = k,m

        while inbound(newx,newy) and matrix[newx][newy] == "*":
            countcross-=1
            newx,newy = newx+x,newy+y

    countcross+=3
    if countcross == 0:
        return "YES"
    return "NO"


for _ in range(1):
    print(solve())