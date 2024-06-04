n,m = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
arr = []
i = 0
prev = 0
for j in list2:
    while i<n and list1[i]<j:
        prev+=1
        i+=1
    arr.append(prev)
for i in arr:
    print(i, end=" ")