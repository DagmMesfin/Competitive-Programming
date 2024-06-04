def dmslinp(datatype):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))

n,k = dmsllinp(int)
arro = dmsllinp(int)

def isthere(mid,k):
    loss = 0
    wanted = 0
    for i in range(n):
        diff = mid - arro[i]
        if diff < 0:
            loss+=diff
        wanted+=diff

    if loss*(k/100) < wanted:
        return -1
    elif loss*(k/100) > wanted:
        return 1
    else:
        return 0
    
left = 0
right = max(arro)

while left+10**-6 < right:
    mid = (left+right)/2
    if isthere(mid,k) <= 0:
        right = mid
    elif isthere(mid,k) > 0:
        left = mid
print(right)


