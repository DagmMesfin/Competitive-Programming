t = int(input())
listo = []
isarrangable = True 

for _ in range(t):
    listo.append(input())

listo.sort(key=lambda elem: len(elem))

for i in range(t-1):
    if listo[i] not in listo[i+1]:
        isarrangable = False
        break

if isarrangable:
    print("YES")
    for i in range(t):
        print(listo[i])
else:
    print("NO")
    