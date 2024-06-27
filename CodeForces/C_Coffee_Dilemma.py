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
    nums = dmsllinp(int)

    sumo = sum(nums)

    if sumo%2:
        return "NO"
    
    sumo //= 2
    memo = {}

    def dp(i,target):
        if i > len(nums)-1:
            return
        if target < 0:
            return False
        if target == 0:
            return True

        if (i,target) not in memo:
            memo[(i,target)] = dp(i+1,target-nums[i]) or dp(i+1,target)
        return memo[(i,target)]
    
    truth = dp(0,sumo)
    return "YES" if truth else "NO"

def solve():
    n = dmslinp(int)
    arr = dmsllinp(int)


for _ in range(1):
    print(solve())