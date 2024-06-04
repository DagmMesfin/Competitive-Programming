n,k = map(int, input().split())

arro = list(map(int, input().split()))

sumo = 0
maxlen = 0
l = 0
for r in range(n):
    sumo+=arro[r]
    while l<r and sumo > k:
        sumo-=arro[l]
        l+=1
    if sumo <= k:
        maxlen= max(maxlen,r-l+1)

print(maxlen)
    
