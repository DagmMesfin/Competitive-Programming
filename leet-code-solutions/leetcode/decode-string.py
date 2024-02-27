class Solution:
    def decodeString(self, s: str) -> str:
        
        def ans(s):
            i = 0
            res = []
            p = 0
            
            while i < len(s):
                num = ""
                if s[i].isnumeric():
                    ch = ""
                    while s[i].isnumeric():
                        num+=s[i]
                        i+=1
                    p = 1
                    num = int(num)
                    i+=1
                    while p!=0:
                        if s[i] == "[":
                            p+=1
                            ch+=s[i]
                        elif s[i] == "]":
                            p-=1
                            if p!=0:
                                ch+=s[i]
                        else:
                            ch+=s[i]
                        i+=1
                    res.append(ans(ch) * num)
                else:
                    res.append(s[i])
                    i+=1

            return "".join(res)
                    


            
        return ans(s)