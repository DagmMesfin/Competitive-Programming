def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    st,target = dmsllinp(int)
    step = 0
    while target>st:
        if not target%2:
            target//=2
        else:
            target+=1
        step+=1
    return step + abs(target-st)

for _ in range(1):
    print(solve())