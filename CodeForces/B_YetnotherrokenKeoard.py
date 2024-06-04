t = int(input())
for _ in range(t):
    stack = defaultdict(str)
    upper = []
    lower = []
    n = list(input())
    while n:
        char = n.pop(0)
        if char == "b":
            if lower:
                lowcase = lower.pop()
                stack.pop(index(lowcase))
        elif char == "B":
            if upper:
                upcase = upper.pop()
                stack.pop(stack.index(upcase))
        else:
            stack.append(char)
            if char.isupper():
                upper.append(char)
            else:
                lower.append(char)
    print("".join(stack))
            
              
    