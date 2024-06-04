t = int(input())
listo = list(map(int, input().split()))
listo.sort()
sumo = sum(listo)
if sumo%2 == 0:
    print(sumo)
else:
    for i in range(len(listo)):
        if listo[i] % 2 == 1:
            print(sumo-listo[i])
            break
        elif listo[i] % 2 == 0 and i == len(listo) - 1:
            print(0)