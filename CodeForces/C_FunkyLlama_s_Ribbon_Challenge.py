import sys, threading

def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))



def main():

    n,a,b,c = dmsllinp(int)
    memo = {}

    def dp(i):
        nonlocal a,b,c
        if i < 0:
            return -1
        if i == 0:
            return 0

        
        if i not in memo:
            aa = dp(i-a)
            ba = dp(i-b)
            ca = dp(i-c)
            aa = aa if aa == -1 else aa+1
            ba = ba if ba == -1 else ba+1
            ca = ca if ca == -1 else ca+1
            memo[i] = max(aa,ba,ca)

        return memo[i]
    
    print(dp(n))
        

    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()