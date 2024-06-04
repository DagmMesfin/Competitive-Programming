n = int(input())

burles = list(map(int, input().split()))
sum = 0
maxo = max(burles)
for bu in burles:
    sum += maxo-bu
print(sum)