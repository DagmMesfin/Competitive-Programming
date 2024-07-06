import sys
input = lambda: sys.stdin.readline().strip()
def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))

def checker(a,h,k):
    for i in range(len(a)-1):
        if a[i]+k-1 < a[i+1]:
            h-=k
        else:
            h-=(a[i+1]-a[i])
    h-=k
    # print("h",h)
    return h<=0




def solve():
    n,h = dmsllinp(int)
    a = dmsllinp(int)
    # print("start")
    l = 0
    r = h
    while l+1<r:
        mid = (l+r)//2
        check = checker(a,h,mid)
        # print(l,r,mid,check)
        if check:
            r = mid
        else:
            l = mid
    return r
    

    


for _ in range(dmslinp(int)):
    print(solve())
    # print("end")


