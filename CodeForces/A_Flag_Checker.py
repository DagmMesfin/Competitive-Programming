def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    r,c = dmsllinp(int)
    arro = []
    
    for _ in range(r):
        inputo = dmslinp()
        arro.append(inputo)
        if len(dmslsplit(inputo,str,set)) != 1:
            return "NO"
    prev = arro[0][0]
    for i in range(1,r):
        if arro[i][0] == prev:
            return "NO"
        prev = arro[i][0]
    

    
    return "YES"


    print(arro)
    
    


for _ in range(1):
    print(solve())