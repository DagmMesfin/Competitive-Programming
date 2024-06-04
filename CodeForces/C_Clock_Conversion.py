def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))
def solve():
    h24 = dmslinp()
    hh,mm = h24.split(":")
    if int(hh) == 0:
        return "12"+":"+mm+" AM"
    if int(hh) < 12:
        return h24+" AM"
    if int(hh) == 12:
        return h24+" M"
    
    hnew = str(int(hh)-12)
    if len(hnew) != 2:
        hnew = "0"+hnew
    return hnew+":"+mm+" PM"
    
for _ in range(dmslinp(int)):
    print(solve())





