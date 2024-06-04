def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def solve():
    n,m,k = dmsllinp(int)
    friends = []
    count = 0
    for i in range(m):
        friends.append(dmslinp(int))
    fedor = dmslinp(int)
    for friend in friends:
        testo = k
        for j in range(n):
            testx = fedor & (1<<j)
            testy = friend & (1<<j)

            if testx^testy:
                testo-=1
        if testo < 0:
            continue
        count+=1
    return count



for _ in range(1):
    print(solve())