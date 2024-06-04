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
    parent = {i:i for i in range(1,len(arro)+1)}

    def find(x):
        if x == parent[x]:
            return x
        parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        x = find(x)
        y = find(y)
        
        if x!= y:
            parent[x] = y

    def connected(x,y):
        return find(x) == find(y)
    
    for i in range(1,len(arro)+1):
        union(i,arro[i-1])
    count = 0
    for i in parent:
        if parent[i] == i:
            count+=1
    return count

for _ in range(1):
    print(solve())