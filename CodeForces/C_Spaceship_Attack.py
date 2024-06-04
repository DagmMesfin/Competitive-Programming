s, b = map(int, input().split())
nums = list(map(int, input().split()))
attack = []
summ = 0
for i in range(b):
    d, g = map(int, input().split())
    attack.append((d, g))
attack.sort()

summ = 0
new = []
for i in range(len(attack)):
    summ += attack[i][1]
    new.append((attack[i][0], summ))

ans = []
for num in nums:
    l, r = -1, len(new)
    while l + 1 < r:
        mid = (l + r) // 2
        if new[mid][0] > num:
            r = mid
        else:
            l = mid
    else:
        ans.append(new[l][1] if l!= -1 else 0)

print(*ans)
