from collections import defaultdict


a = int(input())
b = int(input())
factorization1 = defaultdict(int)
factorization2 = defaultdict(int)
factors = set()
d = 2
i = a+0
j = b+0
while d*d <= i:
    while i%d == 0:
        factorization1[d]+=1
        i//=d
    d+=1
if i>1:
    factorization1[i]+=1
d = 2
while d*d <= j:
    while j%d == 0:
        factorization2[d]+=1
        j//=d
    d+=1
if j>1:
    factorization2[j]+=1

gcd = 1
for factor,v in factorization2.items():
    gcd *= factor*min(factorization1[factor],v) if factor in factorization1 else 1
print(gcd)
print((a*b)//gcd)