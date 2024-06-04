from bisect import bisect_left, bisect_right


for _ in range(int(input())):
    n = int(input())
    points = []
    starts = []
    ends = []
    for i in range(n):
        points.append(tuple(map(int, input().split())))
        ends.append(points[i][1])
    points.sort()
    ends.sort()
    print(points)
    print(ends)
    res = 0
    for i in range(n):
        starto = points[i][0]
        endo = points[i][1]
        pos1 = bisect_right(ends,starto)
        pos2 = bisect_left(ends,endo)
        print(pos1)
        print(pos2)
        print()
        res+=pos2-pos1
    print(res)

    
