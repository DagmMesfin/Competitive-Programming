text1 = input()
text2 = input()
n = len(text1)
m = len(text2)
memo = [[[] for _ in range(m)] for i in range(n)]

def dp(i, j):
    if i >= n or j >= m:
        return []
                
    if memo[i][j] == []:
        if text1[i] == text2[j]:
            res = dp(i+1, j+1)
            res.append(text1[i])
            memo[i][j] = res.copy()

        else:
            left = dp(i+1, j)
            down = dp(i, j+1)
            if len(left) >= len(down):
                memo[i][j] = left
            else:
                memo[i][j] = down
            
    return memo[i][j]
