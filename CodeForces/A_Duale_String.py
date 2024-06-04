def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    s = dmslinp(str)

    if len(s)%2 == 1:
        return "NO"

    if s[:len(s)//2] == s[len(s)//2:]:
        return "YES"
    return "NO"

for _ in range(dmslinp(int)):
    print(solve())