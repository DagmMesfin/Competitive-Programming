def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))



n = dmslinp(int)
a = dmsllinp(int)
ans = [-1]*n

def left(node):
    return node - a[node] >= 0
def right(node):
    return node + a[node] <= n-1 
def dfs(node,parity):
    visited = set()
    stack = []
    stack.append(node)
    while stack: 
        s = stack.pop()
        if (not visited[s]): 
            print(s,end=' ')
            visited[s] = True
        if a[elem]%2 != parity:
            return dist
        if elem not in visited:
            visited.add(elem)
            if left(elem):
                queue.append(elem - a[elem])
            if right(elem):
                queue.append(elem + a[elem])