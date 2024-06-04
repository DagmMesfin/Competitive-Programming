class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        st_pts = [intervals[i][0] for i in range(len(intervals))]
        st_pts_dicto = {st_pts[i]:i for i in range(len(intervals))}

        sorted_st = sorted(st_pts)

        ans = []
        for interval in intervals:
            pos = bisect_left(sorted_st,interval[1])
            ans.append(st_pts_dicto[sorted_st[pos]] if pos < len(intervals) else -1)
        
        return ans