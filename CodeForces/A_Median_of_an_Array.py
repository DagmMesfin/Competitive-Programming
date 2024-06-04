from bisect import bisect_right


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    maxo = arr[-1]
    med = n//2 - 1 if n%2==0 else n//2
    mediano = arr[med]
    pos1 = bisect_right(arr,mediano)

    print(pos1 - (med))