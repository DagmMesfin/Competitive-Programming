def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    n,k = dmsllinp(int)
    a = dmsllinp(int)
    countbit = {i:0 for i in range(31)}
    for i in range(31):
        for numo in a:
            test_num = numo & (1<<i) != 0
            if test_num:
                countbit[i]+=1
    ans = 0
    for i in range(30,-1,-1):
        if  k - n + countbit[i] >= 0:
            ans |= (1<<i)
            k-= n - countbit[i]
            
    return ans



for _ in range(dmslinp(int)):
    print(solve())