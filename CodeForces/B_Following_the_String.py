from bisect import bisect_right

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    count = [0]*26
    count[-1] = 1
    ans = ["a"]
    
    def invert(num):
        return 25-num
    
    for i in range(1,n):
        pos = bisect_right(count,arr[i])-1
        count[pos]+=1
        ans.append(chr(ord("a")+invert(pos)))
    print("".join(ans))

