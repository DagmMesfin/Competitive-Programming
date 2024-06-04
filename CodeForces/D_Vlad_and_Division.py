
from collections import Counter, defaultdict
maxo = 2**31 - 1

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
    dicto = defaultdict(int)

    ans = n

    for i in arro:
        if dicto[i] > 0:
            ans -= 1
            dicto[i] -= 1
            continue
 
        dicto[(i^maxo)] += 1

    return ans



for _ in range(dmslinp(int)):
    print(solve())