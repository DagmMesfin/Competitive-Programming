def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    x = dmslinp(int)
    y = 0
    for i in range(max(x.bit_length(),y.bit_length())):
        testx = x & (1<<i) != 0
        if testx:
            y|=(1<<i)
            break
    while not x^y or not x&y:
        y+=1
    return y


for _ in range(dmslinp(int)):
    print(solve())