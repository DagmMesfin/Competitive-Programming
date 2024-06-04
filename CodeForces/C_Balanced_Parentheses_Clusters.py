def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype = str,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    n = dmslinp(int)
    s = dmslsplit(input())
    parent = {i:i for i in range(2*n)}
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
            parent[y] = x
    def connected(x,y):
        return find(x) == find(y)
    def tuplize(i,c):
        return (i,c)
    
    stack = []

    for i in range(2*n):
        if s[i] == "(":
            stack.append(tuplize(i,0))
        else:
            while stack:
                idx,c = stack.pop()
                if c == 0:
                    union(idx,i)
                    stack.append((i,c+1))
                    break
                else:
                    union(idx,i)
                    stack.append((i,1))
    count = 0
    for x in parent:
        if parent[x]==x:
            count+=1
    return count





for _ in range(dmslinp(int)):
    print(solve())