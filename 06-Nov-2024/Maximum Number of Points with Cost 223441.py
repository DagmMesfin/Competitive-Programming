# Problem: Maximum Number of Points with Cost - https://leetcode.com/problems/maximum-number-of-points-with-cost/

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def get_sum_next(row_orig):
            row = list(row_orig)
            n = len(row)
            for i in range(1, n):
                if row[i-1] - 1 > row[i]:
                    row[i] = row[i-1] - 1

            for i in range(n-2, -1, -1):
                if row[i+1] - 1 > row[i]:
                    row[i] = row[i+1] - 1
            
            return row

        m, n = len(points), len(points[0])
        sum_next = [0] * n
        for row in points:
            curr_point = [sn + r for sn, r in zip(sum_next, row)]
            sum_next = get_sum_next(curr_point)

        return max(curr_point)
        