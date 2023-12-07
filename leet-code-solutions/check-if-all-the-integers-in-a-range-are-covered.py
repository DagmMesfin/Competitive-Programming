class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        #keeps a set of the range from the left and right
        setorange = set([i for i in range(left, right+1)])
        #keeps a set thar are found within the ranges
        setocovered = set()
        

        for i in setorange:
            for j in range(len(ranges)):
                if i<=ranges[j][1] and i>=ranges[j][0]: 
                    setocovered.add(i)
                    break
            #checks if all ranges are covered
            if setorange == setocovered:
                return True
        
        return False