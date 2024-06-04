t = int(input())
for _ in range(t):
    listo = input()
    print(listo) if len(listo) <= 10 else print(f"{listo[0]}{len(listo)-2}{listo[-1]}")