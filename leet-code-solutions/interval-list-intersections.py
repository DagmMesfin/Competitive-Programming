class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersect = []
        A = 0
        B = 0

        while A<len(firstList) and B<len(secondList):
            A_interval = firstList[A]
            B_interval = secondList[B]

            maxo = max(A_interval[0], B_interval[0])
            mino = min(A_interval[1], B_interval[1])

            isIntersect = A_interval[0]<=maxo<=A_interval[1] and B_interval[0]<=maxo<=B_interval[1] and A_interval[0]<=maxo<=A_interval[1] and B_interval[0]<=mino<=B_interval[1]

            if isIntersect:
                intersect.append([maxo,mino])
            
            if A_interval[1] > B_interval[1]:
                B+=1
            elif B_interval[1] > A_interval[1]:
                A+=1
            else:
                A+=1
                B+=1

                
        return intersect

