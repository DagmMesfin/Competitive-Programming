class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if k == n:
            return arr
        
        left,right = 0,n-k
        
        while left+1<right:
            mid = (left+right)//2
            if x - arr[mid] <= arr[mid+k]-x:
                right = mid
            else:
                left = mid
        return arr[left:left+k] if x - arr[left] <= arr[left+k]-x else arr[right:right+k]
