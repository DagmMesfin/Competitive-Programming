n = int(input())

matrix = []
sumo = 0

for i in range(n):
    listo = list(map(int, input().split()))
    matrix.append(listo)

for i in range(n):
    sumo+=matrix[i][i] + matrix[i][n-1-i] + matrix[i][n//2]
    if i == n//2:
        sumo+=sum(matrix[i])

sumo -= 3*matrix[n//2][n//2]

print(sumo)