for _ in range(int(input())):
    x,k = map(int, input().split())
    while True:
        if sum(list(map(int, list(str(x)))))%k==0:
            print(x)
            break
        x+=1
    
