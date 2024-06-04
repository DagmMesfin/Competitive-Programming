
def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    n = dmslinp(int)
    s = dmslinp()
    res = []
    for i in s:
        if res and res[-1] in ["a","e","i","o","u","y"] and i in ["a","e","i","o","u","y"]:
            continue
        res.append(i)
    return "".join(res)

for _ in range(1):
    print(solve())