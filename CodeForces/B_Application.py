n = int(input())

dicto = {}

for _ in range(n):
    request = input()
    if request not in dicto:
        dicto[request] = 0
        print("OK")
    else:
        dicto[request] += 1
        request += str(dicto[request])
        dicto[request] = 0
        print(request)
        