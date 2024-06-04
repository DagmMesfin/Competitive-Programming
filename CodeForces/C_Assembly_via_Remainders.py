def solution():
    n = int(input())
    seta = map(int,input().split())
    ans = [0 for _ in range(n)]
    ans[0] = seta[0]+1

    for idx in range(1,n):
        if idx >= n-1:
            ans[idx] = ans[idx-1]+seta[idx-1]
        else:
            ans[idx] = ans[idx-1]*(seta[idx]//ans[idx-1] + 1)+seta[idx-1]
            
    return ans

testcase = 1
for _ in range(int(input())):
    print(*solution())