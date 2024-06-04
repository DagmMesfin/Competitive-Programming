t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    
    listo = [str(i) for i in range(n,0,-1)]
    liststarto = [str(i) for i in range(1,k+1)]
    liststarto.extend(listo[:n-k])
    
    print(" ".join(liststarto))
