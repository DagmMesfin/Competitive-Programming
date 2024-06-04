text1 = input()
text2 = input()
n = len(text1)
m = len(text2)
memo = [[[] for _ in range(m)] for i in range(n)]


for i in range(n):
    for j in range(m):
        if text1[i] == text2[j]:
            if i == 0 and j-1 >= 0:
                memo[i][j] = memo[i][j-1].copy()