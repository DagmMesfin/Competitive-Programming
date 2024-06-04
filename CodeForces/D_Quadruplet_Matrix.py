from collections import Counter
import math
t = int(input())

for _ in range(t):
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(input())
    
    counter = 0
    
    for i in range(n//2):
        for j in range(math.ceil(n/2)):
            counting = Counter([matrix[i][j], matrix[n-1-j][i], matrix[n-1-i][n-1-j],matrix[j][n-1-i]])
            if counting['0'] == 4 or counting['1'] == 4:
                continue
            counter += min(counting['0'], counting['1'])
             
    print(counter)
        
            