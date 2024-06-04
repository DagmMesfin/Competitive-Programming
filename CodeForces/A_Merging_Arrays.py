n,m = map(int, input().split())
list1 = list(map(str, input().split()))
list2 = list(map(str, input().split()))
arr = []
i = 0
j = 0
while i<n and j<m:
    if int(list1[i])<=int(list2[j]):
        arr.append(list1[i])
        i+=1
    elif int(list2[j])<=int(list1[i]):
        arr.append(list2[j])
        j+=1
if i<n:
    arr.extend(list1[i:])
if j<m:
    arr.extend(list2[j:])
print(' '.join(arr))
    