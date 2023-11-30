move = input()
files = move[0]
rank = int(move[1])
if (files == 'a' or files == 'h') and (rank == 8 or rank == 1):
    print(3)
elif files == 'h' or rank == 8 or rank == 1 or files == 'a':
    print(5)
else:
    print(8)