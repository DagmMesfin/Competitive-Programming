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
    n,m = dmsllinp(int)
    a = dmsllinp(int)
    falld = [0]*n
    pref = [0]*n
    falldrev = [0]*n
    prefrev = [0]*n
    for i in range(1,n):
        falld[i] = max(0,a[i-1]-a[i])
        pref[i] = pref[i-1]+falld[i]
        falldrev[-1-i] = max(0,a[-i]-a[-1-i])
        prefrev[-1-i] = prefrev[-i]+falldrev[-1-i]
    for _ in range(m):
        i,j = dmsllinp(int)
        if j>i:
            print(pref[j-1] - pref[i-1])
        else:
            print(prefrev[j-1] - prefrev[i-1])


for _ in range(1):
    solve()