def dmslinp(datatype):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))
import re
for _ in range(dmslinp(int)):
    n = dmslinp(int)
    stro = dmslinp(str)
    listo = [0]*n
    for i in range(1,n):
        j = listo[i-1]
        while j>0 and stro[i]!=stro[j]:
            j=listo[j-1]
        if stro[i]==stro[j]:
            listo[i] = j+1
    short = n-listo[n-1]

    for i in range(n-1):
        if listo[i]==listo[n-1]:
            short = min(short,n-i-1)
    print(short)
    print(listo)


