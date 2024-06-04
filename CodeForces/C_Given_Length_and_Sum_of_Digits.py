n,s = map(int, input().split())

maxo = []
mino = ["1"]
minleft = []

sumo=s
minusumo = s-1
k = 0
while sumo>0:
    for i in range(9,0,-1):
        tot = sumo//i
        if tot == 0:
            continue
        maxo.extend([str(i)]*tot)
        sumo%=i
        k+=tot
if maxo:
    maxo.extend(["0"]*(n-k))
if n == 1:
    maxo.extend(["0"]*(n-k))
if len(maxo) > n:
    maxo = []

if not maxo or (maxo and maxo[-1] != '0') or (len(maxo) == 1):
    mino = maxo[::-1]
else:
    k = 0

    while minusumo>0:
        for i in range(9,0,-1):
            tot = minusumo//i
            if tot == 0:
                continue
            minleft.extend([str(i)]*tot)
            minusumo%=i
            k+=tot
    minleft.extend(["0"]*(n-k-1))
    mino.extend(minleft[::-1])

maxo = -1 if not maxo else "".join(maxo)
mino = -1 if not mino else "".join(mino)

print(mino,maxo)
