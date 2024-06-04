from bisect import bisect_left

def dmslinp(datatype):
    return datatype(input())
def dmsllinp(datatype,itertype = list):
    return itertype(map(datatype,input().split()))
def dmslsplit(inp,datatype=str,listtype = list):
    inp = str(inp)
    return listtype(map(datatype,inp))

for _ in range(int(input())):
    n = dmslinp(int)
    d = dmsllinp(int)
    
    def merge(left,right):
        left.extend(right)
        return left
        
    

    def merge_seq(arr):

        if len(arr) <= 1:
            return arr
        left = 0
        right = len(arr)
        mid = (left+right)//2
        left_half = merge_seq(arr[:mid])
        right_half = merge_seq(arr[mid:])
        right_copy = sorted(right_half)
        left_copy = sorted(left_half)
        for i in range(len(left_half)):
            pos = bisect_left(right_copy, left_half[i])
            left_half[i]+=pos
        for i in range(len(right_half)):
            pos = bisect_left(left_copy, right_half[i])
            right_half[i]+=pos

        return merge(left_half,right_half)
    print(*merge_seq(d))
        


    

