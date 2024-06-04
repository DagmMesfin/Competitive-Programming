t = int(input())

for _ in range(t):
    n = int(input())
    listo = list(map(int, input().split()))
    listo.sort()
    ispossible = True
    for i in range(1,n):
        if listo[i] == listo[i-1]:
            ispossible = False
            break
    if ispossible:
        print("YES")
    else:
        print("NO")
        
        