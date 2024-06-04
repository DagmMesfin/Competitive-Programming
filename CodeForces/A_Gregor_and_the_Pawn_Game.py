def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    n = dmslinp(int)
    enem = dmslsplit(input(),int,list)
    greg = dmslsplit(input(),int,list)
    count = 0
    def inbound(i):
        return 0<i<n-1

    for i in range(n):
        if greg[i] == 1:
            if not inbound(i):
                if enem[i] == 0:
                    count+=1
                elif (i == n-1 and enem[i-1] == 1):
                    enem[i-1] = -1
                    count+=1

                elif (i == 0 and enem[i+1] == 1):
                    enem[i+1] = -1
                    count+=1

            
            else:
                if enem[i] == 0:
                    count+=1
                else:
                    if enem[i-1] == 1:
                        count+=1
                        enem[i-1]= -1
                    elif enem[i+1] == 1:
                        count+=1
                        enem[i+1] = -1

                    
            
    return count
for _ in range(dmslinp(int)):
    print(solve())