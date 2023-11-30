t = int(input())

for _  in range(t):
    stacko = []
    even = []
    odd = []
    n = int(input())
    listo = input().split()
    for i in range(n):
        numo = int(listo[i])
        if numo%2 == 0:
            even.append(numo)
        else:
            odd.append(numo)
    for i in range(len(even)):
        stacko.append(even[i])
    for j in range(len(odd)):
        stacko.append(odd[j])
    print(*stacko)
    
