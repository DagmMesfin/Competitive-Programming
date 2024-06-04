from heapq import heapify,heappop,heappush

def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    n,k,q = dmsllinp(int)
    t = dmsllinp(int)
    seto = []
    seta = set()

    for i in range(q):
        comm,idx = dmsllinp(int)
        if comm == 1:
            if len(seto) < k:
                heappush(seto,(t[idx-1],idx))
                seta.add(idx)
            elif len(seto) == k:
                if seto[0][0] < t[idx-1]:
                    elem = heappop(seto)
                    seta.remove(elem[1])
                    heappush(seto,(t[idx-1],idx))
                    seta.add(idx)
        elif comm == 2:
            if idx in seta:
                print("YES")
            else:
                print("NO")





for _ in range(1):
    solve()