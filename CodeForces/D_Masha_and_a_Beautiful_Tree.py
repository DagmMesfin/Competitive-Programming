from bisect import bisect_left

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    def merge(left,right):
        nonlocal ans
        if left[0] > right[0]:
            ans+=1
            right.extend(left)
            return right
        left.extend(right)
        return left

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        left = 0
        right = len(arr)
        mid = (left+right)//2
        left_half = merge_sort(arr[:mid])
        right_half = merge_sort(arr[mid:])

        return merge(left_half,right_half)
    
    candidato = merge_sort(p)
    sortedo = sorted(p)
    for i in range(n):
        if candidato[i]!=sortedo[i]:
            print(-1)
            break
        if i==n-1 and candidato[i] == sortedo[i]:
            print(ans)

for _ in range(int(input())):
    solve()
