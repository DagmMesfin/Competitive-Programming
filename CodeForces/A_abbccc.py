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
    n = dmslinp(int)
    s = dmslinp(str)
    ans = []
    k = 1
    i = 0
    while i<n:
        ans.append(s[i])
        i+=k
        k+=1
    return "".join(ans)


for _ in range(1):
    print(solve())