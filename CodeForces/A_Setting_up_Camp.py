def solved():
    a,b,c = map(int, input().split())
    sumo = 0
    sumo+=a
    needed_extro = b//3
    b %= 3
    sumo+=needed_extro
    if b:
        if 3-b <= c:
            c -= 3-b
            sumo+=1
        else:
            return -1
    if c:
        needed_uni = c//3
        c%=3
        sumo+=needed_uni+ (1 if c else 0)
    return sumo

for _ in range(int(input())):
    print(solved())