import sys
import threading
input = lambda: sys.stdin.readline().strip()
def dmslinp(datatype = str):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))


def main():
    n,k,x = dmsllinp(int)

    arr = []

    def dp(i,target):
        if i > k:
            return False
        if target < 0:
            arr.clear()
            return False
        if target == 0:
            return True
        
        if i == x:
            return dp(i+1,target)
        
        arr.append(i)

        return dp(i,target-i) or dp(i+1,target)
        
    ok = dp(1,n)

    print("YES" if ok else "NO")
    if ok:
        print(len(arr))
        print(*arr)







testcase = 1
T = int(input()) if testcase else 1
for _ in range(T):
    if __name__ == 'main':    
        sys.setrecursionlimit(1 << 30)
        threading.stack_size(1 << 27)

        main_thread = threading.Thread(target=main)
        main_thread.start()
        main_thread.join()
    main()
