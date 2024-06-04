class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        #keep the set for the lists of the letters of the same row on the keyboard
        s1 = set("qwertyuiop")
        s2 = set("asdfghjkl")
        s3 = set("zxcvbnm")
        #keep the results
        appendo = []
        #traverses through the lsits of the words
        for i in range(len(words)):
            wordo = words[i].lower()
            isthere = True
            init = wordo[0]
            if init in s1:
                for j in range(1, len(wordo)):
                    if wordo[j] not in s1:
                        isthere = False
                        break
            elif init in s2:
                for j in range(1, len(wordo)):
                    if wordo[j] not in s2:
                        isthere = False
                        break
            elif init in s3:
                for j in range(1, len(wordo)):
                    if wordo[j] not in s3:
                        isthere = False
                        break
            if isthere:
                appendo.append(words[i])
        return appendo

            
            

        
