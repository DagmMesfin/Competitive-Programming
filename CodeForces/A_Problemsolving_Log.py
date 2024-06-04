t = int(input())

for _ in range(t):
    atoz = [i for i in range(1,27)]
    n = int(input())
    stro = input()
    counter = 0
    for i in range(len(stro)):
        index = ord(stro[i]) - ord("A")
        if atoz[index] != 0:
            atoz[index] -= 1
            if atoz[index] == 0:
                counter += 1
    print(counter)