# Problem: E - Machine Testing - https://codeforces.com/gym/513152/problem/E


from math import ceil


def dmslinp(datatype):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))

for _ in range(int(input())):
    n = dmslinp(int)
    h = dmsllinp(int)
    p = dmsllinp(int)
    stack = [(float('inf'),p[0])]
    res = 0

    for i in range(1,n):
        duration = 0
        damage = stack[-1][-1] * (stack[-1][0] - duration)
        while h[i] - damage > 0:
            t,pp = stack.pop()
            h[i] -= pp*(t-duration)
            duration += t-duration
            damage = stack[-1][-1] * (stack[-1][0] - duration)
        duration += ceil(h[i]/stack[-1][-1])
        stack.append((duration,p[i]))
        res = max(res,duration)
    
    print(res)




