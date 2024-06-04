def be_matrix(): 
    listo = []

    for _ in range(5):
        appo = list(map(int, input().split()))
        listo.append(appo)

    for i in range(5):
        for j in range(5):
            if listo[i][j] == 1:
                return(abs(2-i) + abs(2-j))
print(be_matrix())