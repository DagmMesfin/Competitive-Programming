from collections import defaultdict
from math import ceil


n = int(input())
arro = list(map(int, input().split()))
sortedo = sorted(list(enumerate(arro)), key = lambda l:l[1])

numo0 = sortedo[0][1]
numo1 = sortedo[1][1]
diff = abs(sortedo[0][0] - sortedo[1][0])
ans = 0

if diff > 2:
    ans = ceil(numo0/2) + ceil(numo1/2)
elif diff == 2:
    ans = (numo0+numo1)//2 + (numo0+numo1)%2
else:
    mino = min(numo1,numo0)
    maxo = max(numo1,numo0)
    if mino*2 <= maxo:
        ans+=ceil(maxo/2)
    else:
        ans+=maxo-mino
        mino-=(maxo-mino)
        maxo-=2*(maxo-mino)
        ans+=ceil((mino+maxo)/3)

print(ans)
