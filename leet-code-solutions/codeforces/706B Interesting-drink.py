from bisect import bisect_right


n = int(input())

arro = list(map(int, input().split()))
arro.sort()

for _ in range(int(input())):
    q = int(input())
    print(bisect_right(arro,q))