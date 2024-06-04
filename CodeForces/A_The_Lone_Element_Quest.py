from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())
    numo = list(map(int, input().split()))
    for i in range(n - 2):
        if numo[i] == numo[i+1] and numo[i] != numo[i+2]:
            print(i+3)
            break
        if numo[i] == numo[i+2] and numo[i] != numo[i+1]:
            print(i+2)
            break
        if numo[i+1] == numo[i+2] and numo[i+1] != numo[i]:
            print(i+1)
            break