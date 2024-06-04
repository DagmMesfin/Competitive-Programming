t = int(input())
x = 0

for _ in range(t):
    opr = input()
    x += 1 if "++" in opr else -1
print(x)