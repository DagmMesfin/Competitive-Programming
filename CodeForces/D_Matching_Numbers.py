t = int(input())

for _ in range(t):
    overflow = False
    n = int(input())
    if n%2 == 0:
        print("No")
    else:
        print("Yes")
        another_number = 2*n + 2
        for i in range(n):
            if not overflow:
                another_number -= 2
                if another_number-1 == n:
                    overflow = True
            else:
                another_number = 2*n - 1
                overflow = False
            print(str(i+1)+" "+str(another_number))