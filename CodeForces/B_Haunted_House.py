from bisect import bisect_left


for _ in range(int(input())):
    n = int(input())
    s = input()[::-1]

    prefsum = [0]*n
    sufsum = [0]*n
    sumo = 0
    sumo1 = 0
    ans = []
    for i in range(n):
        sumo1+=1 if s[i] == "1" else 0
        sumo+=1 if s[i] == "0" else 0
        prefsum[i] = sumo
        sufsum[i] = sumo1

    for i in range(n):
        pos = bisect_left(prefsum,i+1)
        if pos == n:
            ans.append(-1)
        else:
            if ans:
                ans.append(sufsum[pos]+ans[-1])
            else:
                ans.append(sufsum[pos])
    print(*ans)
