for _ in range(int(input())):
    n,k = map(int, input().split())
    arro = list(map(int, input().split()))
    isthere = True
    prod = arro[0]
    factors = []
    for i in range(1,2024):
        if 2023%i == 0:
            factors.append(i)
    for i in range(1,n):
        if 2023%prod!=0:
            isthere = False
            break
        else:
            prod*=arro[i]
    if 2023%prod!=0:
        isthere = False
    left_factors = []
    if isthere:
        left = 2023//prod
        for _ in range(k):
            if left == 1:
                left_factors.append(1)
                continue
            for i in range(len(factors)-1,-1,-1):
                if left%factors[i] == 0:
                    left_factors.append(factors[i])
                    left = left//factors[i]
                    break
        print("YES")
        print(*left_factors)
    else:
        print("NO")
