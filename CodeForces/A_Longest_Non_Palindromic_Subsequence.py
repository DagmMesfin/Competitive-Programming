
def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))

def ispalindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            return False
    return True

def solve():
    s = dmslinp()
    if not ispalindrome(s):
        return len(s)
    else:
        if s.count(s[0]) == len(s):
            return -1
        else:
            return len(s)-1

    

for _ in range(dmslinp(int)):
    print(solve())