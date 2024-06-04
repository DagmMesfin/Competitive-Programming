t = int(input())
the_main_str = "Yes"
for _ in range(t):
    yes_string = input()
    is_yes = True
    prev = yes_string[0]
    if prev not in the_main_str:
        is_yes = False
    else:
        for i in range(1, len(yes_string)):
            
            if yes_string[i] not in the_main_str:
                is_yes = False
                break
            if the_main_str.index(yes_string[i]) - 1 != the_main_str.index(prev) and the_main_str.index(yes_string[i]) - 1 != the_main_str.index(prev) - len(the_main_str):
                is_yes = False
                break
            prev = yes_string[i]
    
    if is_yes:
        print("YES")
    else:
        print("NO")
            
            
            
        
    