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
    n = dmslinp(int)
    arr = dmsllinp(int)
    lt , rt = dmsllinp(int)
    
    ans = 1
    cursum = sum(arr[lt - 1: rt - 1])


    l = lt - 1 
    r = rt - 2 


    mx = cursum


    for i in range(2 , n + 2):
    
        cursum -= arr[r]
        r -= 1
        l -= 1  

        cursum += arr[l]


        if cursum > mx:
            ans = i
            mx = cursum

    return ans if ans else n

for _ in range(1):
    print(solve())


