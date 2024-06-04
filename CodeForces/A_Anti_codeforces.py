t = int(input())

for _ in range(t):
    codeforces = "codeforces"
    given_string = input()
    diff = 0
    for i in range(len(given_string)):
        if codeforces[i] != given_string[i]:
            diff+=1
    print(diff)