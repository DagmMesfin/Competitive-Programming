from collections import defaultdict
t = int(input())

for _ in range(t):
    sumleft = defaultdict(int)
    sumright = defaultdict(int)
    n,m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(m):
            sumleft[i+j]+=matrix[i][j]
            sumright[i-j]+=matrix[i][j]
    maxo = 0
    for i in range(n):
        for j in range(m):
            maxo = max(maxo,sumleft[i+j]+sumright[i-j] - matrix[i][j])
    print(maxo)
    
            
        
        
    
    