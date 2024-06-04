from collections import Counter


n = list(input())
t = list(input())
arro = list(map(int, input().split()))
def checker(numo):
    countert = Counter(t)
    nu = n.copy()
    for i in range(numo):
        nu[arro[i]-1] = "#"
    nu=[value for value in nu if value != "#"]
    l = 0
    for i in range(len(nu)):
        if l>=len(t):
            return True
        if nu[i] == t[l]:
            l+=1

    return l==len(t)


    


left = 0
right = len(n)

while left+1<right:
    mid = (left+right)//2
    if checker(mid):
        left = mid
    else:
        right = mid

print(left)






