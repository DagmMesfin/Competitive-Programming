n = int(input())
counter = 0
for i in range(2,n+1):

    factorization = set()
    d = 2
    while d*d <= i:
        while i%d == 0:
            factorization.add(d)
            i//=d
        d+=1
    if i>1:
        factorization.add(i)
    if len(factorization) == 2:
        counter+=1

print(counter)

