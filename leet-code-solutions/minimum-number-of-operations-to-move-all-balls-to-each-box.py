class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        wholesteps = []
        for i in range(len(boxes)):
            steps = 0
            for j in range(len(boxes)):
                if boxes[j] == "1":
                    steps+=abs(i-j)
            wholesteps.append(steps)
        return wholesteps
                
