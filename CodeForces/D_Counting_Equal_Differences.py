t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    counter = 0
    diff = set(range(n))
    r = 0
    for di in diff:
        for l in range(n):
            while nums[r] - nums[l] < di:
                r += 1
                if r>=n:
                    break
            if r>=n:
                r = 0
                break
            counter+=n-r
    print(counter)