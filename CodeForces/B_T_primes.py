#author: Dagim Mesfin
from math import sqrt
import sys
input = sys.stdin.readline
def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def prime_sieve(n):
    is_prime = [True for _ in range(n + 1)]
    is_prime[0] = is_prime[1] = False
    i = 2
    res = set()
    while i * i <= n:
        if is_prime[i]:
            j = i * i
            while j <= n:
                is_prime[j] = False
                j += i
        i += 1
    for i in range(len(is_prime)):
        if is_prime[i]:
            res.add(i)
    return res


def solve():
    n = dmslinp(int)
    numo = dmsllinp(int)
    check = prime_sieve(10**6)
    ans = []

    for num in numo:
        if sqrt(num) in check:
            print("YES")
        else:
            print("NO")


# T = dmslinp(int)
T=1

for _ in range(T):
    solve()