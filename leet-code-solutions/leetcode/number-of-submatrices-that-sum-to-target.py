class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        lenr = len(matrix)
        lenc = len(matrix[0])
        presum = []
        ans = 0
        for r in range(lenr):
            listo = []
            sumo = 0
            for c in range(lenc):
                sumo+=matrix[r][c]
                if r==0:
                    listo.append(sumo)
                else:
                    listo.append(sumo + presum[r-1][c])
            presum.append(listo)
        ans = 0

        for r1 in range(lenr):
            for r in range(r1, lenr):
                d = {0:1}
                for c in range(lenc):
                    prefixsum = presum[r][c]
                    if r1 != 0:
                        prefixsum-=presum[r1-1][c]
                    if prefixsum-target in d:
                        ans+=d[prefixsum-target]
                    d[prefixsum] = d.get(prefixsum,0)+1
        return ans
