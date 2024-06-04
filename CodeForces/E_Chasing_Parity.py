from collections import deque


def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    n = dmslinp(int)
    a = dmsllinp(int)
    ans = [-1]*n
    evenidx = []
    oddidx = []
    for i in range(n):
        if a[i]%2:
            oddidx.append(i)
        else:
            evenidx.append(i)

    print(oddidx)
    print(evenidx)

    def left(node):
        return node - a[node] >= 0
    def right(node):
        return node + a[node] <= n-1 
    
    def bfs(nodes,parity):
        visited = set()
        queue = deque(nodes)
        dist = 0
        while queue:
            keepo = list(queue)
            for i in range(len(queue)):
                elem = queue.popleft()
                if a[elem]%2 != parity:
                    ans[elem] = dist
                    visited.add(elem)
                if elem not in visited:
                    if left(elem):
                        queue.append(elem - a[elem])
                    if right(elem):
                        queue.append(elem + a[elem])
            dist+=1
            visited.update(keepo)
        print(ans)

    bfs(oddidx,1)
    bfs(evenidx,0)

    return ans

for _ in range(1):
    print(*solve())