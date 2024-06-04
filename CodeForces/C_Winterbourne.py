t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    listo = list(map(int, input().split()))
    listo.sort(reverse=True)
    sumo = 0
    if n>=m:
        print("NO")
    else:
        for i in range(n-1):
            sumo+= 2*listo[i] if i==0 else listo[i]
        if sumo <= m - n:
            print("YES")
        else:
            print("NO")