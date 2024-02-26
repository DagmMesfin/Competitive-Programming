class Solution:
    def decodeString(self, s: str) -> str:
        strStk = []
        intStk = []
        i = 0
        ans = ""

        while i<len(s):
            count = ""
            if s[i].isnumeric():
                while s[i].isnumeric():
                    count+=s[i]
                    i+=1
                intStk.append(int(count))
            if s[i] == "[":
                if s[i-1].isnumeric():
                    strStk.append(s[i])
                else:
                    strStk.append(s[i])
                    intStk.append(1)
                print(strStk)
            elif s[i] == "]":
                res = ""
                temp = ""
                tempcount = 0
                if intStk:
                    tempcount = intStk.pop()
                while strStk and strStk[-1] != "[":
                    temp = strStk.pop() + temp

                if strStk and strStk[-1] == "[":
                    strStk.pop()

                for _ in range(tempcount):
                    res+=temp
                print(res)
                for j in range(len(res)):
                    strStk.append(res[j])
                
                res = ""
            else:
                strStk.append(s[i])
            i+=1

        while strStk:
            ans = strStk.pop() + ans
            
        return ans