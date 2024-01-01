class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        indexo = []
        def flip(arr, indo):
            if indo < len(arr):
                arr[:indo+1] = arr[:indo+1][::-1]
                return arr
            return []
        maxi = len(arr)
        for i in range(len(arr)-1):
            ind = arr.index(maxi)
            indexo.append(ind+1)
            arr = flip(arr, ind)
            indon = len(arr) - i - 1
            indexo.append(indon+1)
            arr = flip(arr, indon)
            maxi -= 1

        return indexo


            