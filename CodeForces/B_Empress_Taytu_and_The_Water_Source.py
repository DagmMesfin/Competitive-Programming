from math import ceil


for _ in range(int(input())):
    n,k = map(int, input().split())
    d = list(map(int, input().split()))
    a = list(map(int, input().split()))
    def checked(mid):
        timo = 0
        for i in range(n):
            timo += ceil(d[i]/mid) * a[i]
        print("md",mid," timo",timo)
        return timo<=k
    
    left = 0
    right = max(d)

    while left+1<right:
        mid = (left+right)//2
        if checked(mid):
            right = mid
        else:
            left = mid
    
    print(right if checked(right) else -1)
