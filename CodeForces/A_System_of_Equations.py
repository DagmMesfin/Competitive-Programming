n,m = map(int,input().split())
count = 0
for i in range(1,10**6):
    count+=1 if i + n**2 - (2*n*(i**2)) + i**4 == m else 0
print(count)