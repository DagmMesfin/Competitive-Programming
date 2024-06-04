n = int(input())
count = 0
for _ in range(n):
    people = list(map(int, input().split()))
    if sum(people) >1 :
        count+=1
print(count)
    