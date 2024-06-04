from heapq import heappop,heappush,heapify
def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    n = dmslinp(int)
    arro = dmsllinp(int)
    heapo = []
    sumo=0

    for i in range(n):
        if arro[i]:
            heappush(heapo,-arro[i])
        else:
            if heapo:
                sumo-=heappop(heapo)
    return sumo




for _ in range(dmslinp(int)):
    print(solve())