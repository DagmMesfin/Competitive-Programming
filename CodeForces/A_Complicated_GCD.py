def dmslinp(datatype):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
a,b = dmsllinp(int)
if a==b:
    print(a)
elif abs(a-b) > 1:
    print(1)
else:
    print(gcd(a,b))