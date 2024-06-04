
from collections import defaultdict

#test_cases
for _ in range(int(input())):
    n = int(input())
    s = input()
    sumo=0
    dicto = defaultdict(int)
    dicto[0] = 1
    ans = 0
    for i in range(n):
        sumo+=int(s[i])
        dicto[sumo-i-1] += 1
        ans+= dicto[sumo-i-1] - 1

    print(ans)


            