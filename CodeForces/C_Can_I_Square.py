

t = int(input())

for _ in range(t):
    n = int(input())
    listo = list(map(int, input().split()))
    sumo = sum(listo) ** (1/2)
    
    if sumo - int(sumo) == 0:
        print("YES")
    else:
        print("NO")
    