from collections import defaultdict
import sys
input = sys.stdin.readline
def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    n = dmslinp(int)
    arro = dmsllinp(int)
    color = [0]*n

    def dfs(prevnode,node,count):
        if node == prevnode and count == 3:
            return True
        if color[node-1] == 1:
            return False
        color[node-1] = 1

        res = dfs(prevnode,arro[node-1],count+1)
        
        color[node-1] = 0

        return res
    
    for i in range(n):
        if dfs(i+1,i+1,0):
            return "YES"
    return "NO"

for _ in range(1):
    print(solve())
