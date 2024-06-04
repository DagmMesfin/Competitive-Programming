t = int(input())

for _ in range(t):
    n = int(input())
    listo = list(map(int, input().split()))
    l = 0
    r = 1
    even_sum = listo[0]
    odd_sum = listo[1]
    is_add = False
    while l < r and l != n-2:
        print(even_sum)
        print(odd_sum)
        if even_sum == odd_sum:
            is_add = True
            break
        if even_sum > odd_sum:
            if l%2 == 0:
                even_sum-=listo[l]
                l+=1
                continue
            if r%2 == 1:
                odd_sum+=listo[r]
                r+=1
                continue
        elif odd_sum > even_sum:
            if l%2 == 1:
                odd_sum-=listo[l]
                l+=1
                continue
            if r%2 == 0:
                even_sum+=listo[r]
                r+=1
                continue
        else:
            if r%2 == 1:
                odd_sum+=listo[r]
            else:
                even_sum+=listo[l]
    if is_add:
        print("YES")
    else:
        print("NO")
        