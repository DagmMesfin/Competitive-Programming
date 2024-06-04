from collections import Counter, defaultdict


for _ in range(int(input())):
    n,m,k = map(int, input().split())
    arr_n = list(map(int, input().split()))
    arr_m = list(map(int, input().split()))
    countern = [0]*k
    counterm = [0]*k
    wanted_n = wanted_m = 0
    com = 0
    for i in range(n):
        if arr_n[i] <= k:
            countern[arr_n[i]-1]+=1
    for i in range(m):
        if arr_m[i] <= k:
            counterm[arr_m[i]-1]+=1
        
    for i in range(k):
        if counterm[i] and not countern[i]:
            wanted_m+=1
        elif countern[i] and not counterm[i]:
            wanted_n+=1
        elif counterm[i] and countern[i]:
            com+=1

    if wanted_m+wanted_n+com == k:
        if wanted_m == wanted_n:
            print("YES")
        else:
            numo = k//2 - min(wanted_n,wanted_m)
            numo=com-numo
            if numo < 0:
                print("NO")
            else:
                print("YES")
    else:
        print('NO')



