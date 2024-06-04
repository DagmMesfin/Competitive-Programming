def calc(s, char):
    return 2*s.count(char) - len(s)

charo = ['a', 'b', 'c', 'd', 'e']

t = int(input())
for _ in range(t):
    n = int(input())
    listo = []
    count = 0
    for i in range(n):
        listo.append(input())
    
    for j in range(5): 
        counto = 0
        listo.sort(reverse = True, key=lambda x: calc(x,charo[j]))
        print(listo)
        th = 0
        for i in listo:
            th += 2*i.count(charo[j]) - n
            if  th <= 0:
                break
            counto+=1
        count = max(counto,count)
     

    print(count)
    