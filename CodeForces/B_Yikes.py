from bisect import bisect_left


n = int(input())
arro = list(map(int, input().split()))
m = int(input())
query = list(map(int, input().split()))
sumo = 0
prefsum = [0]*n
for i in range(n):
    sumo+=arro[i]
    prefsum[i] = sumo
for i in range(m):
    pos = bisect_left(prefsum,query[i])+1
    print(pos)

