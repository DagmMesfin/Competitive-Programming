t = int(input())

color = input()

if ("CC" in color) or ("MM" in color) or ("YY" in color):
    print("No")
elif "??" in color:
    print("Yes")
elif color[0] == "?" or color[-1] == "?" or ("Y?Y" in color or "M?M" in color or "C?C" in color):
    print("Yes")
else:
    print("No")
