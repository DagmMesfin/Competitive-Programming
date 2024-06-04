t = int(input())

for _ in range(t):
    listo = list(map(int, input().split()))
    passed = 0
    for i in range(1, 4):
        if listo[i] > listo[0]:
            passed+=1
    print(passed)