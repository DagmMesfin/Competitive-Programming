for _ in range(int(input())):
    points = []
    for i in range(4):
        points.append(tuple(map(int, input().split())))
    points.sort()
    mag = (points[0][0] - points[1][0])**2 + (points[0][1] - points[1][1])**2
    print(mag)

