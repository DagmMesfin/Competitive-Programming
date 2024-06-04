def solve():
    n,d = map(str, input().split())
    numo = list(input())
    for i in range(int(n)):
        if int(numo[i]) < int(d):
            return "".join(numo[:i]) + str(d) + "".join(numo[i:])
    return "".join(numo) + str(d)

for _ in range(int(input())):
    print(solve())
