s = input()

larg = "a"
res = []
for i in range(len(s)):
    if s[i] >= larg:
        larg = s[i]

for i in range(len(s)):
    if s[i] == larg:
        res.append(s[i])

print("".join(res))