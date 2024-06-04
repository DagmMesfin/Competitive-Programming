class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        #keeps track of numbers that increase and decreases (strictly)
        increaso = []
        decreaso = []
        ismount = False    #serves as a terminal condition

        #checks if it goes strictly increases and then strictly decreases (terminates for other patterns)
        for i in range(1,len(arr)):
            if arr[i] > arr[i-1]:
                if ismount:
                    return False
                increaso.append(arr[i])
            elif arr[i] < arr[i-1]:
                if not ismount:
                    decreaso.append(arr[i])
                    ismount = True
                else:
                    decreaso.append(arr[i])

            if arr[i] == arr[i-1]:
                return False

        return True if decreaso and increaso else False
                


