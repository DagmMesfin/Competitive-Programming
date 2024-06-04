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
    a = dmslsplit(input())
    b = dmslsplit(input())

    i = 0
    for j in range(len(a)):
        if int(a[j]) == int(b[j]):
            continue
        if not i:
            if int(a[j]) > int(b[j]):
                i^=1
            else:
                a[j],b[j] = b[j],a[j]
                i^=1
                
        else:
            if int(a[j]) > int(b[j]):
                a[j],b[j] = b[j],a[j]

    print("".join(a))
    print("".join(b))

for _ in range(dmslinp(int)):
    solve()