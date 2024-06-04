t = int(input())

for _ in range(t):
    num = list(map(int, input().split()))
    seen = set(num)
    for numo in seen:
        if num.count(numo) == 1:
            print(numo)
    