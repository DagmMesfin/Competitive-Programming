
    n = int(input())
    C = set(["d","b","c"])
    V = set(["a", "e"])
    stingo = input()
    stacko = []
    res = []
    for i in range(n):
        if not stacko:
            stacko.append(stingo[i])
        elif stingo[i] in V:
            stacko.append(stingo[i])
        elif stingo[i] in C and stacko[-1] in V:
            if i+1 < n and stingo[i+1] in V:
                if not res:
                    res.extend(stacko)
                else:
                    res.append(".")
                    res.extend(stacko)
                stacko.clear()
                stacko.append(stingo[i])
            else:
                stacko.append(stingo[i])
                
        elif stingo[i] in C and stacko[-1] in C:
            if not res:
                res.extend(stacko)
            else:
                res.append(".")
                res.extend(stacko)
            stacko.clear()
            stacko.append(stingo[i])
    if stacko:
        if res:
            res.append(".")
        res.extend(stacko)
    print("".join(res))
    