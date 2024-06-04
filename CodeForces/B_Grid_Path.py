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
    n,m,k = dmsllinp(int)
    the_grid = [[0 for _ in range(m)] for _ in range(n)]

    for x in range(n):
        for y in range(m):
            if y == 0:
                the_grid[x][y] = x
                continue
            the_grid[x][y] += the_grid[x][y-1] + x+1
    
    return 'YES' if the_grid[-1][-1] == k else "NO"
            
            
            
            


for _ in range(dmslinp(int)):
    print(solve())