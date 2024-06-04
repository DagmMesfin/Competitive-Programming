def dmslinp(datatype):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))

for _ in range(dmslinp(int)):
    n = dmslinp(int)
    listo = [int(bin(i)[2:]) for i in range(2**6)]
    incre = 2
    if n not in listo:
        while incre<len(listo) and n>1:
            while not n%listo[incre]:
                n//=listo[incre]
            incre+=1
    
        if n==1:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
 
