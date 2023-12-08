class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        directory_duplicates = defaultdict(list)
        lastres = []
        def directory_appender(patho, dicto):
            dir_path = patho.split()
            finalised_path = dir_path[0]+"/"
            keyo = ""
            for j in range(1,len(dir_path)):
                finalised_path += dir_path[j][:dir_path[j].rfind("txt")+3]
                keyo = dir_path[j][dir_path[j].rfind("txt")+3:]
                dicto[keyo].append(finalised_path)
                finalised_path = dir_path[0]+"/"

        for i in range(len(paths)):
            directory_appender(paths[i], directory_duplicates)


        for key,val in directory_duplicates.items():
            if len(val) != 1:
                lastres.append(val)
        

        
        return lastres