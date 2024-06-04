def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    n = dmslinp(int)
    ex = [0,0,0]
    words = ["chest","biceps","back"]
    exercises = dmsllinp(int)
    for i in range(n):
        ex[i%3]+=exercises[i]
    maxo = max(ex)
    return words[ex.index(maxo)]



for _ in range(1):
    print(solve())