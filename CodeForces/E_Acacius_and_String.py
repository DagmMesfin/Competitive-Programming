import sys
input = lambda: sys.stdin.readline().strip()
def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def count_subo(s,v):
    n = len(s)
    ans = 0
    for i in range(n-6):
        if s[i:i+7] == v: 
            ans += 1
    return ans
 
def solve():
    n = dmslinp(int)
    s = dmslinp()
    subo = "abacaba"

    if count_subo(s,subo) == 1:
        s = s.replace('?','x')
        print("Yes")
        print(s)
        return
   
    for i in range(n-6):
        cur = list(s)
        for x in range(i,i+7):
            if cur[x] == '?':
                cur[x] = subo[x - i]

        cur = "".join(cur)
        if count_subo(cur,subo) == 1:
            cur = cur.replace('?','x')
            print("Yes")
            print(cur)
            return
       
    print("No")
 
for _ in range(dmslinp(int)):
    solve()