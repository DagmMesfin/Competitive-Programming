def solved():
    n,h = map(int, input().split())
    sumo = 0
    for i in range(n):
        sumo+=max(map(int, input().split()))
    if sumo >= h:
        return "YES"
    else:
        return "NO"
    
for _ in range(int(input())):
    print(solved())