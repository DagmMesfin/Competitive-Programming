t = int(input())

for _ in range(t):
    ciphered_string = input()
    dechiphered_string = ciphered_string[:2]
    for i in range(2, len(ciphered_string), 2):
            dechiphered_string+=ciphered_string[i+1]
    print(dechiphered_string)