from collections import Counter
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
    n,k = dmsllinp(int)
    s = dmslinp()
    counter = Counter(s)
    ans = float("inf")
    for i in range(ord("A"),ord("A")+k):
        ans = min(ans,counter[chr(i)])
    return ans*k

for _ in range(1):
    print(solve())