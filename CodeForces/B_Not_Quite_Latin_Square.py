t = int(input())

for _ in range(t):
    seen = set()
    for i in range(3):
        call = input()
        if call[0] == "?":
            seen.add(call[1])
            seen.add(call[2])
        elif call[1] == "?":
            seen.add(call[0])
            seen.add(call[2])
        elif call[2] == "?":
            seen.add(call[0])
            seen.add(call[1])
    if 'A' not in seen:
        print("A")
    elif 'B' not in seen:
        print("B")
    elif 'C' not in seen:
        print("C")
    
        
            
            
        
    
    