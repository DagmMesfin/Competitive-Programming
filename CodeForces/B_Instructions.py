import sys, threading

def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))

def main():
    t = dmslinp(int)
    for i in range(t):
        n = dmslinp(int)
        arro = dmsllinp(int)
        memo = {}
        ans = 0

        def dp(i):
            if i >= n:
                return 0
            
            if i not in memo:
                memo[i] = dp(i+arro[i])+arro[i]
        
            return memo[i]
        
        for i in range(n):
            if i not in memo:
                memo[i] = dp(i)

            ans = max(ans,memo[i])

        print(ans)

    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()