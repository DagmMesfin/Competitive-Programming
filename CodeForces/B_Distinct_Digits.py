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
    s = dmslinp(int)
    ans = []
    for i in range(9,0,-1):
        if s-i >= 0:
            ans.append(str(i))
            s-=i
        if s <= 0:
            break
    return "".join(ans[::-1])


for _ in range(dmslinp(int)):
    print(solve())