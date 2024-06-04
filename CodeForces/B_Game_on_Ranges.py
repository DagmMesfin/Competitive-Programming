def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    n = dmslinp(int)
    ranges = set()
    ans = []
    marked = [False]*(n+1)
    for _ in range(n):
        ranges.add(dmsllinp(int,tuple))
    for l,r in ranges:
        for d in range(l,r+1):
            if (l==d or (l,d-1) in ranges) and (r==d or (d+1,r) in ranges):
                ans.append([l,r,d])
                break
    return ans

    
    

for _ in range(dmslinp(int)):
    arro = solve()
    for i in range(len(arro)):
        print(*arro[i])