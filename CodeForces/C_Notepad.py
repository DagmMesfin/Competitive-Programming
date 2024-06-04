t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    is_typable = False
    dicto = {}
    for i in range(n-1):
        sec = s[i:i+2]
        if sec in dicto:
            if dicto[sec] < i - 1:
                is_typable = True
                break
        else:
            dicto[sec] = i
    if is_typable:
        print("YES")
    else:
        print("NO")