from collections import defaultdict, deque


def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    n  = dmslinp(int)

    parent = {i:i for i in range(1,n+1)}
    size = {i:1 for i in range(1,n+1)}
    merger = {i:[i] for i in range(1,n+1)}
    ans = 2*n
    def find(x):
        stk = []
        stk.append(x)
        while stk:
            if stk[-1] == parent[stk[-1]]:
                break
            stk.append(parent[x])
            x = parent[x]
        ans = stk[-1]
        while stk:
            k = stk.pop()
            parent[k] = ans
        return ans


    
    def union(x, y):
        x = find(x)
        y = find(y)
        
        if x!= y:
            if size[x] >= size[y]:
                parent[y] = x
                size[x]+=size[y]
                merger[x].extend(merger[y])
                del merger[y]
            else:
                parent[x] = y
                size[y]+=size[x]
                merger[y].extend(merger[x])
                del merger[x]
                

    def connected(x,y):
        return find(x) == find(y)
    

    for j in range(n-1):
        x,y = dmsllinp(int)
        union(x,y)
    ans = []
    for i in merger:
        ans.extend(merger[i])
    return ans



for _ in range(1):
    print(*solve())