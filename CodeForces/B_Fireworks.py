for _ in range(int(input())):
    a,b,c = map(int, input().split())
     
    f = (c // a) + 1
    
    s = (c // b) + 1
    print(f+s)