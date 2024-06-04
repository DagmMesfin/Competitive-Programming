for _ in range(int(input())):
    n,m = map(int , input().split())
    st = list(input())
    t = list(input())

    sums = 0
    init = 0

    for i in range(m):
        sums += ord(t[i])
        init += ord(st[i])
    
    if sums == init:
        print("YES")
    else:
        for i in range(m , n):
            init += ord(st[i])
            init -= ord(st[i-m])

            if sums == init:
                print("YES")
                break
        else:
            print("NO")

