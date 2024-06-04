t = int(input())
for _ in range(t):
    n = input()
    for i in range(8):
        if chr(i+ord('a')) == n[0]:
            continue
        print(f"{chr(i+ord('a')) + n[1]}")
    for j in range(8):
        if j+1 == int(n[1]):
            continue
        print(n[0]+str(j+1))
